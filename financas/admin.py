from django.contrib import admin
from .models import DespesasFixas

admin.site.register(DespesasFixas)

def __str__(self):
  return self.nome