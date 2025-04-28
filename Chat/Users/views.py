from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

#Users

def Cadastro_User(request):
    return HttpResponse(request,'sucesso')

def Login_User(request):
    return HttpResponse(request,'sucesso')

def Salvar_Novo_User(request):
    return HttpResponse(request,'sucesso')

def Salvar_User_Editado(request,Id):
    return HttpResponse(request,'sucesso')

def Excluir_User(request,Id):
    return HttpResponse(request,'sucesso')

#Friends

def Send_Friend_Request(request,id_to_friend):
    return HttpResponse(request,'sucesso')

def Accept_Friend_request(request,id_to_friend):
    return HttpResponse(request,'sucesso')

def Delete_Friend(request,id_to_unfriend):
    return HttpResponse(request,'sucesso')