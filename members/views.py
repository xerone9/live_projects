from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_users(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, ("There was an error"))
            return redirect('login_users')
    else:
        return render(request, 'login.html', {})


def logout_users(request):
    logout(request)
    messages.info(request, ("You are successfully loged out"))
    return redirect('login_users')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, ("Registration Successful...."))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register_user.html', {'form': form})

