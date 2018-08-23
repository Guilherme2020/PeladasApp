from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from users import serializers
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
# Create your views here.
class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'user-detail'
    queryset =  User.objects.all()
    serializer_class = serializers.UserSerializerDetail
    model = User


class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializerDetail

    def get_object(self):
        return self.request.user


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user_name': user.username,
        'user_email': user.email,
        'user_id': user.id

            },
                    status=HTTP_200_OK)

