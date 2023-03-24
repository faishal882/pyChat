from .serializers import UserSerializers, LoginSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

# Create your views here.
@api_view(["POST"])
def register_user(request):
    """
    User Creation Function.
    ----
    POST Data
    request.data =  {
        username: "John",
        email: "john@mail.com",
        password: "xxxxxxxx"
    }
    """
    user_serializer = UserSerializers(data=request.data)
    if user_serializer.is_valid(raise_exception=True):
        user = user_serializer.create(request.data)
        if user:
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=200)
    return Response(user_serializer.errors, status=400)


@csrf_exempt
@api_view(["POST"])
def login_user(request):
    """
    User Authentication Function.
    ----
    POST Data
    request.data =  {
        username: "fm",
        password: "xxxxxxxx"
    }
    """
    serializer = LoginSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.validated_data["user"]
        auth.login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "Token": token.key,
                "user": UserSerializers(user).data,
            },
            status=200,
        )
    return Response(serializer.errors, status=400)