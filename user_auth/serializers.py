from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, data):
        password = data.get("password", None)
        if not password:
            raise exceptions.ValidationError("password is required !")
        if User.objects.filter(email__iexact=data["email"]).count() >= 1:
            raise exceptions.ValidationError("Email Already in use !!")
        user = User.objects.create_user(**data)
        user.save()
        data = user
        return data

    def update(self, subs, validated_data):
        subs.username = validated_data.get("username", subs.username)
        subs.first_name = validated_data.get("first_name", subs.first_name)
        subs.last_name = validated_data.get("last_name", subs.last_name)
        subs.email = validated_data.get("email", subs.email)
        subs.save()
        return UserSerializers(subs).data
    


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data["user"] = user
            else:
                raise exceptions.ValidationError(
                    "Unable to login with given credentials."
                )
        else:
            raise exceptions.ValidationError("Must Provide Email and Password both !!")
        return data