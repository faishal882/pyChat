from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import  CustomUserCreationForm, LoginForm

@login_required(login_url='/login')
def home_view(request):
    users = User.objects.all()
    print(users)
    return render(request, 'home/index.html', {"users": users})


@login_required(login_url='/login')
def chatroom(request, user):
    users = User.objects.all()
    messages = []
    return render(request, 'home/chat_screen.html', {"users": users, "messages": messages, "user": user})

def  user_register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if  request.POST and form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect("/")
    return render(request, 'user/register.html', {'form':form})

def login_view(request, *args, **kwargs):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/")
    return render(request, 'user/login.html', {'form':form})
    


def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect("/login")