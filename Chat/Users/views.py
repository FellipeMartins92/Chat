from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from . import forms, models
# Create your views here.

#Users

def Cadastro_User(request):
    return render(request,'Users/Cadastro_User.html')

def Login_User(request):
    return render(request,'Users/Login_User.html')

def Editar_User(request,Id):
    user = models.User.objects.get(id=Id)
    return render(request,'Users/Editar_User.html',{'user':user})

def Validate_Login_User(request):
    if request.method == 'POST':
        form = forms.Login_User_Form(request.POST)
        if form.is_valid() and models.User.Validate_User(request.POST.get('mail'),request.POST.get('password')):
            return HttpResponse('Sucesso')
        
    return HttpResponse('Deu Ruim')

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
    user = get_object_or_404(models.User, id=Id)

    if request.method == 'POST':
        form = forms.Edit_User_Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado com sucesso!')
            return HttpResponse('Sucesso') 
        else:
            messages.error(request, 'Erro ao Editar. Verifique os dados e tente novamente.')
            return HttpResponse('Erro') 

    return HttpResponse('Erro')

def Excluir_User(request,Id):
    user = models.User.objects.filter(id=Id).first()
    if user:
        user.delete() 
        return HttpResponse('Deletado')
    else:
        return HttpResponse('Erro')

#Friends
    
def Add_Friends(request):
    return render(request, 'Friends/Add_Friends.html')            

def Send_Friend_Request(request,id_to_friend):
    return HttpResponse(request,'sucesso')

def Accept_Friend_request(request,id_friend_request):
    return HttpResponse(request,'sucesso')

def Delete_Friend(request,id_to_unfriend):
    return HttpResponse(request,'sucesso')