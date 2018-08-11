from rest_framework import serializers

from .models import Pelada, Configuracao, Jogador, Time


class PeladaSerializers(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pelada-detail', read_only=True)

    class Meta:
        model = Pelada
        fields = '__all__'


class PeladaSerializerDetail(serializers.HyperlinkedModelSerializer):
    jogadores = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='jogador-detail'
    )
    times = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='time-detail'
    )
    class Meta:
        model = Pelada
        fields = '__all__'


class ConfiguracaoSerializerDetail(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'

class JogadoresSerializerDetail(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'

class TimesSerializerDetail(serializers.HyperlinkedModelSerializer):
    jogadores = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='jogador-detail'
    )
    class Meta:
        model = Time
        fields = '__all__'
