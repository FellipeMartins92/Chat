from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Cadastro_Group(request):
    return HttpResponse(request,'sucesso')

def Excluir_Group(request):
    return HttpResponse(request,'sucesso')

def Adicionar_Ao_Group(request,Id):
    return HttpResponse(request,'sucesso')

def Excluir_Do_Group(request,Id):
    return HttpResponse(request,'sucesso')