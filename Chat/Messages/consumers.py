import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from urllib.parse import parse_qs
from .models import *

connected_users = {}

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        query_params = parse_qs(self.scope["query_string"].decode())
        self.user_id = query_params.get("user_id", [None])[0]

        if not self.user_id:
            await self.close()
            return

        if self.room_group_name not in connected_users:
            connected_users[self.room_group_name] = set()

        connected_users[self.room_group_name].add(str(self.user_id))

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        if self.room_group_name in connected_users:
            connected_users[self.room_group_name].discard(self.user_id)        

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        receiver_id = data['receiver_id']
        sender_id = data['sender_id']

        receiver_online = str(receiver_id) in connected_users.get(self.room_group_name, set())

        await self.save_message(sender_id, receiver_id, message, receiver_online)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id,
                'read': receiver_online
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_id': event['sender_id'],
            'read': event['read']
        }))        

    @sync_to_async
    def save_message(self, sender_id, receiver_id, message, read=False):        
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        
        messages_to_user.objects.create(
            id_sender=sender,
            id_receiver=receiver,
            message=message,
            read=read
        )