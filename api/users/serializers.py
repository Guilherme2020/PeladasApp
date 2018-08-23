import jwt

from calendar import timegm
from datetime import datetime, timedelta

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class DonoSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email')
