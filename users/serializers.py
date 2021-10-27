
from django.db.models import Q
from rest_framework import exceptions, serializers
from django.contrib.auth import authenticate
from users.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password:
            user = User.objects.filter(
                (Q(username=username))
            ).first()
            if user and authenticate(username = username,password = password):
                data["user"] = user
                
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.AuthenticationFailed({"username": [msg]})
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError({"username": [msg]})
        return data




