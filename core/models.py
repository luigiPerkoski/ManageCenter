from django.contrib.auth.models import User
from django.db import models

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    horario_entrada = models.IntegerField()
    intervalo = models.IntegerField()
    horario_almoco = models.IntegerField()
    horario_saida = models.IntegerField()
    duracao_intervalo = models.IntegerField()
    atividade = models.BooleanField()
    cor = models.CharField(max_length=20, choices=[("cinza", "Cinza"), ("amarelo", "Amarelo"), ("verde", "Verde"), ("vermelho", "Vermelho")])

    def __str__(self):
        return f"Funcionario {self.usuario.username}"

class Lider(models.Model):
    funcionarios = models.ManyToManyField(Funcionario)

    def __str__(self):
        return "Lider"