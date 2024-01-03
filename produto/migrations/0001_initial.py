# Generated by Django 5.0 on 2023-12-25 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('SP', 'shape'), ('RD', 'roda'), ('RL', 'rolamento'), ('PR', 'parafuso'), ('TK', 'truck'), ('LX', 'lixa'), ('AS', 'acessorios')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]
