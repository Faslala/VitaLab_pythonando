from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            messages.warning(request, 'As senhas não coincidem!')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.warning(request, 'A senha deve conter 6 caracteres ou mais!')
            return redirect('/usuarios/cadastro')
        
        try:
            # Verificar se o usuário já existe
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já está em uso!')
                return redirect('/usuarios/cadastro')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email já está em uso!')
                return redirect('/usuarios/cadastro')
            
            # Criar usuário
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
            messages.success(request, 'Cadastro efetuado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro interno: {e}')
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/cadastro')


def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        
    if user:
        login(request, user)
        return redirect('/admin')
    else:
        messages.warning(request, 'Usuário ou senha inválidos')
        return redirect('/usuarios/login')