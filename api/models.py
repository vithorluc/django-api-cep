from django.db import models

# Create your models here.
class Cep(models.Model):
  cep = models.CharField(max_length=9, unique=True)
  logradouro = models.CharField(max_length=255, blank=True)
  complemento = models.CharField(max_length=255, blank=True)
  bairro = models.CharField(max_length=255, blank=True)
  localidade = models.CharField(max_length=255, blank=True)
  uf = models.CharField(max_length=2, blank=True)
  ibge = models.CharField(max_length=10, blank=True)
  gia = models.CharField(max_length=4, blank=True)
  ddd = models.CharField(max_length=3, blank=True)
  siafi = models.CharField(max_length=4, blank=True)