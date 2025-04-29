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
    id_friend_one = models.ForeignKey(User, related_name='sent_friend', on_delete=models.CASCADE)
    id_friend_two = models.ForeignKey(User, related_name='received_friend', on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS)


