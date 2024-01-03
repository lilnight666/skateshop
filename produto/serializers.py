from rest_framework import serializers
from .models import produto
from django.contrib.auth.models import User

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = ('id','nome','preco','estoque','categoriaa',' stripe_product_i','file','url')
        
