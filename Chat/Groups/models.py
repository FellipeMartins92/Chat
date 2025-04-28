from django.db import models
from Users.models import *

# Create your models here.

class GroupChat(models.Model):
    name = models.CharField(max_length=100)

class UsersInGroup(models.Model):
    id_group = models.ManyToManyField(GroupChat)
    id_user = models.ManyToManyField(User)

