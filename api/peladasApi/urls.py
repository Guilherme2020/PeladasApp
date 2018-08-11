"""peladasApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function:p from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from players.views import *

obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()

from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import refresh_jwt_token,obtain_jwt_token, verify_jwt_token
from players.views import PeladaViewSet, PeladaDetailViewSet,TimeDetailViewSet ,ConfiguracaoDetailViewSet, PeladaListUser, JogadorDetailViewSet
from users import views as views_user
from rest_framework_swagger.views import get_swagger_view
# from players.views import
from players.views import ConfiguracaoList, CreateTimes

schema_view = get_swagger_view(title='Pelada API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/jwt/token/get',obtain_jwt_token),
    path('api/jwt/token/refresh',refresh_jwt_token),
    path('api/jwt/token/verify',verify_jwt_token),
    path('auth/',include('rest_framework_social_oauth2.urls')),
    path('api/peladas/', PeladaViewSet.as_view()),
    path('api/user-peladas/', PeladaListUser.as_view()),
    path('api/pelada/<int:pk>', PeladaDetailViewSet.as_view(), name='pelada-detail'),
    path('api/configuracao/<int:pk>', ConfiguracaoDetailViewSet.as_view(), name='configuracao-detail'),
    path('api/jogador/<int:pk>', JogadorDetailViewSet.as_view(), name='jogador-detail'),
    path('api/time/<int:pk>', TimeDetailViewSet.as_view(), name='time-detail'),
    path('api/user/<int:pk>', views_user.UserDetailViewSet.as_view(), name='user-detail'),
    path('api/docs/', schema_view),
    path('api/configuracao/', ConfiguracaoList.as_view(), name='configuracao-list'),
    path('api/jogadores/', JogadoresList.as_view(), name='configuracao-list'),
    path('api/times/', TimeList.as_view(), name='configuracao-list'),
    path('api/pelada/<int:pk>/create_times/', CreateTimes.as_view({'post':'create_times'}), name="create-times")
]
