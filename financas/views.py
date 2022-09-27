from django.shortcuts import render, redirect
from . models import DespesasFixas

def home(request):
    despesasfixas = DespesasFixas.objects.all()
    return render(request, "index.html", {"despesasfixas": despesasfixas})

def salvar(request):
    descricao = request.POST.get('descricao')
    data_inicio = request.POST.get('data_inicio')
    data_fim = request.POST.get('data_fim')
    valor = request.POST.get('valor')
    DespesasFixas(descricao=descricao, data_inicio=data_inicio,
    data_fim=data_fim, valor=valor).save()
    despesasfixas = DespesasFixas.objects.all()
    return render(request, "index.html", {"despesasfixas": despesasfixas})

def editar(request, id):
    despesasfixas = DespesasFixas.objects.get(id=id)
    return render(request, "update.html", {"despesasfixas": despesasfixas})

def update(request, id):
    descricao = request.POST.get('descricao')
    data_inicio = request.POST.get('data_inicio')
    data_fim = request.POST.get('data_fim')
    valor = request.POST.get('valor')
    despesasfixas = DespesasFixas.objects.get(id=id)
    despesasfixas.descricao = descricao
    despesasfixas.data_inicio = data_inicio
    despesasfixas.data_fim = data_fim
    despesasfixas.valor = valor
    despesasfixas.save()
    return redirect(home)

def delete(request, id):
    despesasfixas = DespesasFixas.objects.get(id=id)
    despesasfixas.delete()
    return redirect(home)

def consulta_despesas_fixas(request):
    despesasfixas = DespesasFixas.objects.all()
    valor_total = 0
    for d in despesasfixas:
        valor_total = float(d.valor) + valor_total
    return render(request, 'consulta_despesas_fixas.html', {'despesasfixas': despesasfixas, 'valor_total': valor_total})

def cadastro_despesa_fixa(request):
    return render(request, 'cadastro_despesa_fixa.html')
