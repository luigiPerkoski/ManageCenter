from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import FormLogin, FormRegister

def view_login(request):
    #*===============================================================
    form = FormLogin()

    if request.method == 'POST':
        form = FormLogin(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        
        try:
            login(request, user)
            return redirect('index')
        except:
            form.add_error('password', 'Usuario ou Senha incorreto')

    context = {'form': form}
    return render(request, 'pages/login.html', context)


def view_register(request):
    #*===============================================================

    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                form.add_error('username', 'Este nome de usuário já está em uso.')
                return render(request, 'pages/cadastro.html', {'form': form})

            try:
                validate_password(password)
            except:
                form.add_error('password', 'senha invalida')
                return render(request, 'pages/register.html', {'form': form})
            
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=password
            )
            return redirect('/')
    else:
        form = FormRegister()

    return render(request, 'pages/register.html', {'form': form})