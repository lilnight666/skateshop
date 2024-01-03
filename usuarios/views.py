from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import UsuarioSerializer


def cadastro(request):
    if request.user.is_authenticated:
        return redirect()
    if request.method == "GET":
        return render(request)
    elif request.method== "POST":
        nome= request.POST.get('nome')
        email= request.POST.get('email')
        senha= request.POST.get('senha')
        confirmar_senha= request.POST.get('confirmar_senha')

        if len(nome.strip())==0 or len(email.strip())==0 or len(senha.strip())==0 or len(confirmar_senha.strip())==0:
            messages.add_message(request, constants.ERROR, 'prencha todos os campos')
            return render(request)
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'digite as senhas da mesma forma')
            return render(request)
        try:
            user = User.objects.create_user(
                username= nome,
                email=email,
                password=senha  

            )
            messages.add_message(request, constants.SUCCESS, 'usuario criado com sucesso')
            return render(request)
        except:
            messages.add_message(request, constants.ERROR, 'erro interno no sistema')
            return render(request)
            

            



        
def logar(request):
    if request.user.is_authenticated:
        return redirect()
    if request.method == "GET":
        return render(request, )

    elif request.method== "POST":
        nome= request.POST.get('nome')
        senha= request.POST.get('senha')
        user= authenticate(
            username=nome,
            password= senha
        )
        if user is not None:
            login(request, user)
            return redirect()
        else:
            messages.add_message(request, constants.ERROR, 'usuario ou senha incorretos')
            return render(request, )

def sair(request):
    logout(request)
    return redirect()




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
    
