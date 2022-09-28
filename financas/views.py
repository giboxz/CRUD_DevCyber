from django.shortcuts import render, redirect
from . models import DespesasFixas

def home(request):
    despesas_fixas = DespesasFixas.objects.all()
    return render(request, "index.html", {"despesasfixas": despesas_fixas})

def salvar(request):
    descricao = request.POST.get('descricao')
    valor = request.POST.get('valor')
    DespesasFixas(descricao=descricao, valor=valor).save()
    despesasfixas = DespesasFixas.objects.all()
    return render(request, "index.html", {"despesasfixas": despesasfixas})

def editar(request, id):
    despesasfixas = DespesasFixas.objects.get(id=id)
    return render(request, "update.html", {"despesasfixas": despesasfixas})

def update(request, id):
    descricao = request.POST.get('descricao')
    valor = request.POST.get('valor')
    despesas_fixas = DespesasFixas.objects.get(id=id)
    despesas_fixas.descricao = descricao
    despesas_fixas.valor = valor
    despesas_fixas.save()
    return redirect(home)

def delete(request, id):
    despesas_fixas = DespesasFixas.objects.get(id=id)
    despesas_fixas.delete()
    return redirect(home)

def consulta_despesas_fixas(request):
    despesas_fixas = DespesasFixas.objects.all()
    valor_total = 0
    for d in despesas_fixas:
        valor_total = float(d.valor) + valor_total
    return render(request, 'consulta_despesas_fixas.html', {'despesasfixas': despesas_fixas, 'valor_total': valor_total})

def cadastro_despesa_fixa(request):
    return render(request, 'cadastro_despesa_fixa.html')