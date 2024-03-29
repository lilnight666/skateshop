# Generated by Django 5.0 on 2024-01-02 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0007_alter_categoria_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='product_files/'),
        ),
        migrations.AddField(
            model_name='produto',
            name='stripe_product_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_price_id', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
        migrations.DeleteModel(
            name='pedido',
        ),
    ]
