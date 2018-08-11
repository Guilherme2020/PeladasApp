from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer, VerifyJSONWebTokenSerializer, \
    RefreshJSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView
from players import mixins
from .models import Pelada, Configuracao, Jogador, Time
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, exceptions
from players import permissions
from .permissions import PublicEndpoint
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import detail_route


# Create your views here.

class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.
    Returns a JSON Web Token that can be used for authenticated requests.
    """

    throttle_scope = 'obtain-token'
    throttle_classes = (ScopedRateThrottle,)
    serializer_class = JSONWebTokenSerializer

class VerifyJSONWebToken(JSONWebTokenAPIView):
    """
    API View that checks the veracity of a token, returning the token if it
    is valid.
    """

    throttle_scope = 'obtain-token'
    throttle_classes = (ScopedRateThrottle,)
    serializer_class = VerifyJSONWebTokenSerializer


class RefreshJSONWebToken(JSONWebTokenAPIView):
    """
    API View that returns a refreshed token (with new expiration) based on
    existing token
    If 'orig_iat' field (original issued-at-time) is found, will first check
    if it's within expiration window, then copy it to the new token
    """

    throttle_scope = 'obtain-token'
    throttle_classes = (ScopedRateThrottle,)
    serializer_class = RefreshJSONWebTokenSerializer



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
        user = self.request.user
        configuracoes = Configuracao.objects.filter(pelada__dono=user)
        return Response(status=status.HTTP_200_OK,
                        data=serializers.ConfiguracaoSerializerDetail(configuracoes, many=True, context={'request': request}).data)

class JogadoresList(mixins.FilteringAndOrderingMixin, generics.ListCreateAPIView):
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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        pelada = request.data['pelada'].split('/')[5]
        if Pelada.objects.filter(dono=request.user, pk=pelada).count() > 0:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"status":"Voce só pode adicionar jogadores as suas peladas"},status=status.HTTP_400_BAD_REQUEST)




class PeladaListUser(generics.ListCreateAPIView):

    serializer_class = serializers.PeladaSerializerDetail

    def get_queryset(self):
        return Pelada.objects.filter(dono=self.request.user)

    def validate(self, data):
        errors = {}
        dono = data.get('dono')

        if self.request.user != dono:
            errors['error'] = 'O usuario não pode criar'
            raise serializers.ValidationError(errors)

        return data

    def post(self, request, *args, **kwargs):
        dono = request.data['dono']
        dono = dono.split('/')
        tamanho = len(dono)
        dono = int(dono[tamanho - 1])
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if dono == self.request.user.id:

            if serializer.is_valid():
                pelada = serializer.save()

                return Response(status=status.HTTP_201_CREATED,
                                    data=serializers.PeladaSerializers(pelada, context={'request': request}).data)
        else:
            raise exceptions.NotAcceptable(detail=('O usuario só pode criar peladas para ele.'))


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