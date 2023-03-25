from django.urls import path
from .views import home_view, login_view, chatroom, user_register_view, logout_view

app_name = 'chat'

urlpatterns = [
   path("", home_view, name='chat_view'),
   path("login/", login_view, name='login_view'),
   path('logout/', logout_view, name='logout_view'),
   path("register/", user_register_view, name='register_view'),
   path('chat/<str:user>', chatroom, name='chatroom_view')
]