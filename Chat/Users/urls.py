from django.urls import path
from . import views

urlpatterns = [

    #Usuário
    path('Cadastro', views.Cadastro_User,name='Cadastro'),
    path('Salvar_Novo_User', views.Salvar_Novo_User,name='Salvar_Novo_User'),
    path('Login', views.Login_User,name='Login'),
    path('Validate_Login_User', views.Validate_Login_User,name='Validate_Login_User'),
    path('Editar/<int:Id>/', views.Editar_User,name='Editar'),
    path('Salvar_User_Editado/<int:Id>/', views.Salvar_User_Editado,name='Salvar_User_Editado'),

    #Friends

    path('Add_Friends', views.Add_Friends,name='Adicionar_Amigos'),

]