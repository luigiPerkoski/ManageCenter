# Generated by Django 5.0.4 on 2024-05-02 23:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_entrada', models.IntegerField()),
                ('intervalo', models.IntegerField()),
                ('horario_almoco', models.IntegerField()),
                ('horario_saida', models.IntegerField()),
                ('duracao_intervalo', models.IntegerField()),
                ('atividade', models.BooleanField()),
                ('cor', models.CharField(choices=[('cinza', 'Cinza'), ('amarelo', 'Amarelo'), ('verde', 'Verde'), ('vermelho', 'Vermelho')], max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcionarios', models.ManyToManyField(to='core.funcionario')),
            ],
        ),
    ]
