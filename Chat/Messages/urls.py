from django.urls import path
from . import views

urlpatterns = [
    path('Messages', views.Messages,name='Messages'),
]