from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.core import validators
import re


# Create your models here.

class Jogador(models.Model):
    DIREITO, ESQUERDO = "D", "E"
    MELHOR_PE = (
        (DIREITO, ("Direito")),
        (ESQUERDO, ("Esquerdo")),
    )
    NOTA_CHOICES = tuple([(x, x) for x in range(1, 6)])

    nome = models.CharField(max_length=255, )
    email = models.EmailField('E-mail', unique=True, blank=True, null=True)
    phone_number = models.CharField(verbose_name=("Phone Number"), max_length=16, blank=True, null=True,
                                    validators=[validators.RegexValidator(re.compile('^\+\d{13}|\(\d{2}\)[ ]\d{5}-\d{4}$'),
                                    ("A phone number must be on this format: (99) 99999-9999"), "invalid")])
    rating = models.SmallIntegerField(verbose_name='Nota', choices=NOTA_CHOICES, default=3)
    pelada = models.ForeignKey('Pelada', related_name='jogadores', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        jogador = self
        super(Jogador, self).save()
        checkin = Checkin.objects.filter(jogador=jogador)
        if checkin.count() == 0:
            Checkin.objects.create(jogador=jogador, status="D", pelada=jogador.pelada)


class Time(models.Model):
    nome = models.CharField(max_length=255)
    jogadores = models.ManyToManyField(Jogador, related_name='times')
    pelada = models.ForeignKey('Pelada', related_name='times', on_delete=models.CASCADE)


class Partida(models.Model):
    gols = models.ForeignKey("Gol", on_delete=models.CASCADE)
    times = models.ForeignKey("Time", related_name="partidas", on_delete=models.CASCADE)


class Checkin(models.Model):
    DISPONIVEL, NA_PELADA, REMOVIDO = "D", "P", "R"
    STATUS = (
        (DISPONIVEL, ("Disponivel")),
        (NA_PELADA, ("Na pelada")),
        (REMOVIDO, ("Removido")),
    )
    jogador = models.OneToOneField("Jogador", on_delete=models.CASCADE, related_name="checkin")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS)
    pelada = models.ForeignKey('Pelada', related_name='checkins', on_delete=models.CASCADE)


class HistoricoChecking(models.Model):
    DISPONIVEL, NA_PELADA, REMOVIDO = "D", "P", "R"

    STATUS = (
        (DISPONIVEL, ("Disponivel")),
        (NA_PELADA, ("Na pelada")),
        (REMOVIDO, ("Removido")),
    )
    jogador = models.ForeignKey("Jogador", on_delete=models.CASCADE, related_name="historico")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS)
    to_status = models.CharField(max_length=1, choices=STATUS)


class Pelada(models.Model):
    nome = models.CharField(max_length=200)
    configuracao = models.OneToOneField('Configuracao', on_delete=models.CASCADE)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='peladas')

    @property
    def create_times(self):
        if self.configuracao.tipo_sorteio == self.configuracao.ORDEM_CHEGADA:

            if self.times.all().count() == 0:
                qtd_jogadores = self.jogadores.all().filter(checkin__status="D").count()
                jogadores = self.jogadores.all().filter(checkin__status="D")
                qtd_por_time = self.configuracao.qtd_jogadores
                pelada = self
                time1 = Time.objects.create(nome="Time1", pelada=pelada)

                jogadores_time_1 = jogadores.order_by('?')[:int(qtd_por_time)]
                for jogador in jogadores_time_1:
                    time1.jogadores.add(jogador)
                    checkin = jogador.checkin
                    checkin.status = "P"
                    checkin.save()
                jogadores_time_2 = jogadores.filter(~Q(id__in=[o.id for o in jogadores_time_1]))
                time2 = Time.objects.create(nome="Time2", pelada=pelada)
                for jogador in jogadores_time_2:
                    time2.jogadores.add(jogador)
                    checkin = jogador.checkin
                    checkin.status = "P"
                    checkin.save()
                return True
            else:
                return False


class Gol(models.Model):
    jogador = models.OneToOneField("Jogador", related_name='gols_jogador', on_delete=models.CASCADE)
    time = models.OneToOneField("Time", related_name='gols_time', on_delete=models.CASCADE)


class Configuracao(models.Model):
    TEMPO1, TEMPO2 = "T1", "T2"
    TEMPOS = (
        (TEMPO1, ("1 Tempo")),
        (TEMPO2, ("2 Tempos")),
    )
    LIMITE_GOLS = (
        ("1", "1 GOL"),
        ("2", "2 GOLS"),
        ("3", "3 GOLS"),
        ("4", "4 GOLS"),
        ("5", "5 GOLS"),
    )
    QTD_JOGADORES = (
        ("5", "5 Jogadores"),
        ("6", "6 Jogadores"),
        ("7", "7 Jogadores"),
        ("8", "8 Jogadores"),
        ("9", "9 Jogadores"),
        ("10", "10 Jogadores"),
        ("11", "11 Jogadores"),
        ("12", "12 Jogadores"),
    )
    ORDEM_CHEGADA, SEM_SORTEIO, NIVEL_TECNICO = 'O', 'S', 'N'
    TIPO_SORTEIO = (
        (ORDEM_CHEGADA, "Ordem de chegada"),
        (SEM_SORTEIO, "Sem sorteio"),
        (NIVEL_TECNICO, "Nivel Tecnico")
    )
    tempos = models.CharField(max_length=1, choices=TEMPOS)
    tempo_duracao = models.TimeField()
    limite_gols = models.CharField(max_length=1, choices=LIMITE_GOLS)
    qtd_jogadores = models.CharField(max_length=1, choices=QTD_JOGADORES)
    tipo_sorteio = models.CharField(max_length=1, choices=TIPO_SORTEIO)


def add_jogador(jogador):
    checkin = jogador.checkin
    checkin.status = Checkin.NA_PELADA
    checkin.save()
