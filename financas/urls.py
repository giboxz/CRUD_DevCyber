from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete, cadastro_despesa_fixa, consulta_despesas_fixas

urlpatterns = [
    path("", home),
    path("cadastro_despesa_fixa/", cadastro_despesa_fixa, name='cadastro_despesa_fixa'),
    path("consulta_despesas_fixas/", consulta_despesas_fixas, name='consulta_despesas_fixas'),
    path("salvar/", salvar, name="salvar"),
    path("editar/<int:id>", editar, name='editar'),
    path("update/<int:id>", update, name='update'),
    path("delete/<int:id>", delete, name='delete')
]