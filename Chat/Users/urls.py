from django.urls import path
from . import views

urlpatterns = [
    path('Cadastro', views.Cadastro_User,name='Cadastro'),
    path('Salvar_Novo_User', views.Salvar_Novo_User,name='Salvar_Novo_User'),
]