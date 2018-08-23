from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

from players import mixins
from .models import Pelada, Configuracao, Jogador, Time
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, exceptions
from players import permissions
from .permissions import PublicEndpoint, IsOwnerPelada
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import detail_route
from rest_framework import viewsets, authentication, permissions

from django.http import JsonResponse

# Create your views here.




class PeladaViewSet(mixins.FilteringAndOrderingMixin, generics.ListAPIView ):

    permission_classes = (PublicEndpoint,)
    name = 'pelada-list'
    serializer_class = serializers.PeladaSerializers
    model = Pelada
    filter_fields = ('dono__username',)
    search_fields = ('nome',)
    queryset = Pelada.objects.all()

  


class PeladaDetailViewSet(mixins.IsOwnerPeladaMixin,  generics.RetrieveUpdateDestroyAPIView):

    name = 'pelada-detail'
    queryset =  Pelada.objects.all()
    serializer_class = serializers.PeladaSerializerDetail
    model = Pelada

class JogadorDetailViewSet(mixins.IsPeladaMixin,generics.RetrieveUpdateDestroyAPIView):

    name = 'jogador-detail'
    queryset =  Jogador.objects.all()
    serializer_class = serializers.JogadoresSerializerDetail
    model = Jogador

class TimeDetailViewSet(mixins.IsPeladaMixin,generics.RetrieveUpdateDestroyAPIView):

    name = 'times-detail'
    queryset =  Time.objects.all()
    serializer_class = serializers.TimesSerializerDetail
    model = Time

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        jogadores = instance.jogadores.all()
        for jogador in jogadores:
            checking = jogador.checkin
            checking.status = "D"
            checking.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PeladaConfiguracaoDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'configuracao-pelada-detail'
    queryset =  Pelada.objects.all()
    serializer_class = serializers.ConfiguracaoSerializerDetail
    model = Pelada

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        configuracao = instance.configuracao
       
        return Response(status=status.HTTP_200_OK,data=serializers.ConfiguracaoSerializerDetail(configuracao,context={'request': request}).data)

class ConfiguracaoDetailViewSet(mixins.IsPeladaMixin,generics.RetrieveUpdateDestroyAPIView):

    name = 'configuracao-detail'
    queryset =  Configuracao.objects.all()
    serializer_class = serializers.ConfiguracaoSerializerDetail
    model = Configuracao

class TimeList(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView):

    serializer_class = serializers.TimesSerializerDetail
    queryset =  Time.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        times = Time.objects.filter(pelada__dono=user)
        return Response(status=status.HTTP_200_OK,
                        data=serializers.TimesSerializerDetail(times, many=True, context={'request': request}).data)


class ConfiguracaoList(generics.ListCreateAPIView):

    serializer_class = serializers.ConfiguracaoSerializerDetail
    queryset =  Configuracao.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous:
             return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data=({"Warning": "Voce nao esta autenticado"}))
        else:
            user = self.request.user
            print(self.request)
            configuracoes = Configuracao.objects.filter(pelada__dono=user)
        return Response(status=status.HTTP_200_OK,
                        data=serializers.ConfiguracaoSerializerDetail(configuracoes, many=True, context={'request': request}).data)

class JogadoresList(generics.ListCreateAPIView):
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = ('nome',)
    filter_fields = ('rating',)
    serializer_class = serializers.JogadoresSerializerDetail
    queryset =  Jogador.objects.all()


    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user = self.request.user
        queryset = queryset.filter(pelada__dono=user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        jogador = Jogador.objects.filter(pelada__dono=user)
        return Response(serializer.data)

    



class PeladaListUser(generics.ListCreateAPIView):
    authentication = (authentication.SessionAuthentication)
    serializer_class = serializers.PeladaSerializers
    queryset = Pelada.objects.all()
    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous:
             return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data=({"Warning": "Voce nao esta autenticado"}))
        else:
            user = self.request.user
            peladas = Pelada.objects.filter(dono=user)
        return Response(status=status.HTTP_200_OK,
                        data=serializers.PeladaSerializers(peladas, many=True, context={'request': request}).data)



    def validate(self, data):
        errors = {}
        dono = data.get('dono')

        if self.request.user != dono:
            errors['error'] = 'O usuario não pode criar'
            raise serializers.ValidationError(errors)

        return data

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)


class CreateTimes(viewsets.ViewSet):

    @detail_route(methods=['post'])
    def create_times(self, request, pk=None):
            pelada = self.get_queryset().get(pk=pk)
            if pelada.create_times == True:
                return Response({"status":"Times criados"},status=status.HTTP_200_OK)
            if pelada.create_times == False:
                return Response({"status":"Times ja criados ou sua solicitacao possui erro"},status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        qs = Pelada.objects.all()
        return qs