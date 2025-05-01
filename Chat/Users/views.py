from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from . import forms
from Users.models import *
# Create your views here.

#Users

def Cadastro_User(request):
    return render(request,'Users/Cadastro_User.html')

def Login_User(request):
    return render(request,'Users/Login_User.html')

@custom_login_required
def Logout_User(request):
    request.session.flush()
    return redirect('Login')

@custom_login_required
def Editar_User(request,Id):
    user = User.objects.get(id=Id)
    return render(request,'Users/Editar_User.html',{'user':user})

def Validate_Login_User(request):        
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')

        try:
            user = User.objects.get(mail=mail, password=password)
            request.session['user_id'] = user.id
            request.session['name'] = user.name
            request.session['mail'] = user.mail
            if user.picture and hasattr(user.picture, 'url'): 
                request.session['picture'] = user.picture.url
            else:
                request.session['picture'] = '/static/images/default.png'
            return redirect('/')  
        except User.DoesNotExist:
            return HttpResponse('Credenciais inválidas.')

    return render(request, 'Users/Login_User.html')

def Salvar_Novo_User(request):
    if request.method == 'POST':
        form = forms.Cadastro_User_Form(request.POST)
        if form.is_valid() and User.Validate_Single_Mail(request.POST.get('mail')):
            form.save()
            return redirect('/Login')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')

    return redirect('Cadastro') 

@custom_login_required
def Salvar_User_Editado(request,Id):
    user = get_object_or_404(User, id=Id)

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password') 
        password_to_verify = request.POST.get('password_to_verify')
        picture_url = request.FILES.get('picture')

        if name:
            user.name = name
        if password == password_to_verify:
            user.password = password
        if picture_url:
            user.picture = picture_url

        user.save()

        if request.session.get('user_id') == user.id:
            request.session['name'] = user.name
            request.session['mail'] = user.mail
            if user.picture and hasattr(user.picture, 'url'):
                request.session['picture'] = user.picture.url

        return redirect('User_Page', Id)        

    return HttpResponse('Erro')

@custom_login_required
def Excluir_User(request,Id):
    user = User.objects.filter(id=Id).first()
    if user:
        user.delete() 
        return HttpResponse('Deletado')
    else:
        return HttpResponse('Erro')
    
@custom_login_required
def User_Page(request,Id):
    user = User.objects.get(id=Id)
    return render(request,"Users/User_Page.html",{"user":user})

#Friends
    
@custom_login_required  
def Add_Friends(request):
    users = User.objects.exclude(id=request.session['user_id'])

    if request.method =='GET':
        name = request.GET.get('name', '')

        if name:
            users = users.filter(name=name)

    return render(request, 'Friends/Add_Friends.html',{"users":users})            

@custom_login_required
def Send_Friend_Request(request,id_to_friend):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Accept_Friend_request(request,id_friend_request):
    return HttpResponse(request,'sucesso')

@custom_login_required
def Delete_Friend(request,id_to_unfriend):
    return HttpResponse(request,'sucesso')