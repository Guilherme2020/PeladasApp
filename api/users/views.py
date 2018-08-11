from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from users import serializers
# Create your views here.
class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'user-detail'
    queryset =  User.objects.all()
    serializer_class = serializers.UserSerializerDetail
    model = User

