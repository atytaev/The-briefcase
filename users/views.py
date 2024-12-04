from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# Регистрация
def register(request):
    if request.user.is_authenticated:
        return redirect('film_list')

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    elif request.method == 'GET':
        form = CustomUserCreationForm()

    return render(
        request,
        'register.html',
        context={'form': form},
    )

# Авторизация
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('film_list')  # Перенаправление на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Выход
def user_logout(request):
    logout(request)
    return redirect('film_list')  # Перенаправление на главную страницу

