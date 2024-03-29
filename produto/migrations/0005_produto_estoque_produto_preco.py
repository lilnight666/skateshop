# Generated by Django 5.0 on 2023-12-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_rename_categoria_produto_categoriaa'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
