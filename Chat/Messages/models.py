from django.db import models
from Users.models import *
from Groups.models import *


# Create your models here.

class messages_to_user(models.Model):
    id_sender = models.ManyToManyField(User)
    id_receiver = models.ManyToManyField(User)
    message = models.CharField(255)

class messages_to_group(models.Model):
    id_group = models.ManyToManyField(GroupChat)
    id_sender = models.ManyToManyField(User)
    message = models.CharField(255)