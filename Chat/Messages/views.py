from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from Users.models import *
from .models import *

# Create your views here.

#Chat

@custom_login_required
def Messages(request):
    users = User.objects.all()

    if request.method == 'GET' and request.GET.get('name', ''):
        users = users.filter(name__contains=request.GET.get('name', ''))

    id_receiver = request.GET.get('id_receiver')
    user_id = request.session.get('user_id')
    messages = []

    if id_receiver:
        messages = messages_to_user.objects.filter(
            Q(id_sender=user_id,   id_receiver=id_receiver) |
            Q(id_sender=id_receiver, id_receiver=user_id)
        ).order_by('sent')

    return render(request, "Messages.html", {
        "users": users,
        "messages": messages,
        "id_receiver": id_receiver,
    })

@custom_login_required
def Atualizar_Messages(request, id_receiver):
    user_id = request.session.get('user_id')

    messages = messages_to_user.objects.filter(
        Q(id_sender=user_id,   id_receiver=id_receiver) |
        Q(id_sender=id_receiver, id_receiver=user_id)
    ).order_by('sent')

    data = [{
        'message':    m.message,
        'id_sender':  m.id_sender.id,
        'id_receiver':m.id_receiver.id,
    } for m in messages]

    return JsonResponse({'messages': data})

#Mensagens

@custom_login_required
def Mandar_Message_To_UserChat(request):
    if request.method == 'POST':
        user_receiver = User.objects.get(id=request.POST.get('id_receiver'))
        user = User.objects.get(id=request.session.get('user_id'))
        message = request.POST.get('mensagem')

        if user_receiver and message:
            chat = messages_to_user()
            chat.message = message
            chat.id_receiver = user_receiver
            chat.id_sender = user
            chat.save()

        return redirect(f'/Messages/?id_receiver={user_receiver.id}')

    return redirect('Messages')


@custom_login_required
def Delete_Message_From_UserChat(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Mandar_Message_To_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Delete_Message_From_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')