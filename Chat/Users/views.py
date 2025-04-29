from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from . import forms, models
# Create your views here.

#Users

def Cadastro_User(request):
    return render(request,'Users/Cadastro_User.html')

def Login_User(request):
    return HttpResponse(request,'sucesso')

def Salvar_Novo_User(request):
    if request.method == 'POST':
        form = forms.Cadastro_User_Form(request.POST)
        if form.is_valid() and models.User.Validate_Single_Mail(request.POST.get('mail')):
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')
    return redirect('Cadastro') 

def Salvar_User_Editado(request,Id):
    return HttpResponse(request,'sucesso')

def Excluir_User(request,Id):
    return HttpResponse(request,'sucesso')

#Friends

def Send_Friend_Request(request,id_to_friend):
    return HttpResponse(request,'sucesso')

def Accept_Friend_request(request,id_friend_request):
    return HttpResponse(request,'sucesso')

def Delete_Friend(request,id_to_unfriend):
    return HttpResponse(request,'sucesso')