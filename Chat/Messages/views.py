from django.shortcuts import render
from django.http import HttpResponse
from Users.models import *
from .models import *

# Create your views here.

#Chat

@custom_login_required
def Messages(request):
    users = User.objects.all()
    messages = [] 

    if request.method == 'GET' and request.GET.get('id_receiver') is None:
        name = request.GET.get('name', '')
        if name:
            users = users.filter(name__icontains=name)
    
    if request.method == 'GET' and request.GET.get('id_receiver') is not None:
        id_receiver = request.GET.get('id_receiver')
        try:
            messages = messages_to_user.objects.filter(id_receiver=id_receiver)  # Retorna todas as mensagens
        except:
            messages = [] 

    return render(request, "Messages.html", {"users": users, "messages": messages})


#Mensagens

@custom_login_required
def Mandar_Message_To_UserChat(request):
    if request.method == 'POST':
        user_receiver = User.objects.get(id=request.POST.get('id_receiver'))
        user = User.objects.get(id=request.session.get('user_id'))
        message = request.POST.get('mensagem')

        if user_receiver and message:
            chat = messages_to_user()
            chat.message = message
            chat.id_receiver = user_receiver
            chat.id_sender = user
            chat.save()

        return redirect(f'/Messages/?id_receiver={user_receiver.id}')

    return redirect('Messages')


@custom_login_required
def Delete_Message_From_UserChat(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Mandar_Message_To_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Delete_Message_From_GroupChat(request,Id):
    return HttpResponse(request,'sucesso')