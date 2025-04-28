from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    ativo = models.BooleanField(default=True)

class Friends(models.Model):
    STATUS = {
        ("1", "Pending"),
        ("2", "Accepted"),
    }
    id_friend_one = models.ManyToManyField(User)
    id_friend_two = models.ManyToManyField(User)
    status = models.CharField(max_length=3, choices=STATUS)


