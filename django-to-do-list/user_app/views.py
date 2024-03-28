from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class Sign_up(APIView):
    def post(self, request):
        data = request.data.copy()
        data['username'] = data.get("email")
        new_user = User(**data)
        try:
            new_user.full_clean()
            new_user = User.objects.create_user(**data)
            token = Token.objects.create(user=new_user)
            login(request, new_user)
            return Response({"user": new_user.email, "token": token.key}, status=HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.message_dict, status=HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        data = request.data.copy()
        user = authenticate(username=data.get("email"),
                            password=data.get("password"))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({"user": user.email, "token": token.key}, status=HTTP_200_OK)
        return Response("No user matching these credentials", status=HTTP_404_NOT_FOUND)


class Logout(APIView):
    def post(self, request):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        request.user.auth_token.delete()
        logout(request)
        return Response(status=HTTP_204_NO_CONTENT)
