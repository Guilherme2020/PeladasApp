from rest_framework import serializers
from users.serializers import DonoSerializerDetail
from .models import Pelada, Configuracao, Jogador, Time






class ConfiguracaoSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'

class PeladaSerializers(serializers.ModelSerializer):
    configuracao = ConfiguracaoSerializerDetail()

    class Meta:
        model = Pelada
        fields = '__all__'

class JogadoresSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'

class TimesSerializerDetail(serializers.ModelSerializer):
    jogadores = JogadoresSerializerDetail(many=True, read_only=True)

    class Meta:
        model = Time
        fields = '__all__'


class PeladaSerializerDetail(serializers.ModelSerializer):
    jogadores = JogadoresSerializerDetail(many=True, read_only=True)
    # times = TimesSerializerDetail(many=True, read_only=True)
    # configuracao = ConfiguracaoSerializerDetail(many=False)
    dono = DonoSerializerDetail()

    class Meta:
        model = Pelada
        exclude = ('configuracao',)
