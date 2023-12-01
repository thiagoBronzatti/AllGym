from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass 

class GymDetail(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.CharField(max_length=640)
    endereco = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=640)
    imagem2 = models.CharField(max_length=640)
    linkacademia = models.CharField(max_length=640)
    horario = models.CharField(max_length=640)
    fitdance = models.BooleanField(default=True, blank=True, null=True)
    nutricionista = models.BooleanField(default=True, blank=True, null=True)
    arcondicionado = models.BooleanField(default=True, blank=True, null=True)
    personal  = models.BooleanField(default=True, blank=True, null=True)
    natação  = models.BooleanField(default=True, blank=True, null=True)
    pilates = models.BooleanField(default=True, blank=True, null=True)
    spinning = models.BooleanField(default=True, blank=True, null=True) 
    vestiario = models.BooleanField(default=True, blank=True, null=True)
    estacionamento = models.BooleanField(default=True, blank=True, null=True)
