from django.shortcuts import render
from django.contrib.auth.models import User

def home_view(request):
    users = User.objects.all()
    print(users)
    return render(request, 'home/index.html', {"users": users})

def login_view(request):
    return render(request, 'user/login.html')

def chatroom(request, user):
    users = User.objects.all()
    messages = []
    return render(request, 'home/chat_screen.html', {"users": users, "messages": messages, "user": user})