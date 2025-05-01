from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Chat

def Messages(request):
    return render(request,"Messages.html")



#Mensagens

def Mandar_Message_To_UserChat(request,Id):
    return HttpResponse(request,'sucesso')

def Delete_Message_From_UserChat(request,Id):
    return HttpResponse(request,'sucesso')

def Mandar_Message_To_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')

def Delete_Message_From_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')