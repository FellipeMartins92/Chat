from django.shortcuts import render
from django.http import HttpResponse

from Users.models import custom_login_required

# Create your views here.

@custom_login_required
def Cadastro_Group(request):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Excluir_Group(request):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Adicionar_Ao_Group(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Excluir_Do_Group(request,Id):
    return HttpResponse(request,'sucesso')