# Generated by Django 3.2.4 on 2021-06-09 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('login', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('nome', models.CharField(max_length=25)),
                ('departamento', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=25)),
                ('descricao', models.TextField(null=True)),
                ('data', models.DateTimeField()),
                ('tecnico', models.CharField(max_length=15)),
                ('prioridade', models.CharField(max_length=15, null=True)),
                ('status', models.CharField(max_length=15, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]