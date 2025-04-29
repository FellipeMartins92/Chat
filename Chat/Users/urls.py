from django.urls import path
from . import views

urlpatterns = [
    path('Cadastro', views.Cadastro_User,name='Cadastro'),
    path('Salvar_Novo_User', views.Salvar_Novo_User,name='Salvar_Novo_User'),
    path('Login', views.Login_User,name='Login'),
    path('Validate_Login_User', views.Validate_Login_User,name='Validate_Login_User'),
]