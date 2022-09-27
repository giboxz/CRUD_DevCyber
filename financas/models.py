from django.db import models

class DespesasFixas(models.Model):
    valor = models.CharField(max_length=10)
    data_inicio = models.CharField(max_length=50)
    data_fim = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
