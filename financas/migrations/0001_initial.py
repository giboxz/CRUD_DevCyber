# Generated by Django 4.1.1 on 2022-09-28 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DespesasFixas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DespesasVariaveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=10)),
                ('data_inicio', models.CharField(max_length=50)),
                ('data_fim', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
