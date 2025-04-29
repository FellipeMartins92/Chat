from django.db import models
from Users.models import *
from Groups.models import *


# Create your models here.

class messages_to_user(models.Model):
    id_sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    id_receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

class messages_to_group(models.Model):
    id_group = models.ManyToManyField(GroupChat)
    id_sender = models.ForeignKey(User, related_name='sent_messages_group', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)