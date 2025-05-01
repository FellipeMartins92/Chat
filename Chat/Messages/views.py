from django.shortcuts import render
from django.http import HttpResponse
from Users.models import *

# Create your views here.

#Chat

@custom_login_required
def Messages(request):
    users = User.objects.all()

    if request.method =='GET':
        name = request.GET.get('name', '')

        if name:
            users = users.filter(name=name)

    return render(request,"Messages.html",{"users":users})


#Mensagens

@custom_login_required
def Mandar_Message_To_UserChat(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Delete_Message_From_UserChat(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Mandar_Message_To_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Delete_Message_From_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')