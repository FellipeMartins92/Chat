from django.urls import path
from . import views

urlpatterns = [
    path('Messages/', views.Messages,name='Messages'),
    path('Enviar_Mensagem', views.Mandar_Message_To_UserChat, name='Enviar_Mensagem'),
    path('Atualizar_Messages/<int:id_receiver>/', views.Atualizar_Messages, name='Atualizar_Messages')
]