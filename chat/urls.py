from django.urls import path
from .views import home_view, login_view, chatroom

app_name = 'chat'

urlpatterns = [
   path("", home_view),
   path("login", login_view),
   path('chat/<str:user>', chatroom)
]