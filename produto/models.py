from django.db import models
from .choices import choicescategoria

class Categoria(models.Model):
    title= models.CharField(max_length=30,choices=choicescategoria.choices)
    def __str__(self):
        return self.title
     
class produto(models.Model):
    nome= models.CharField(max_length=25)
    preco= models.DecimalField(max_digits=8,decimal_places=2)
    estoque=models.DecimalField(max_digits=8,decimal_places=2)
    categoriaa=models.ManyToManyField(Categoria)
    stripe_product_id = models.CharField(max_length=100)
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField()
    
    
    def __str__(self):
        return self.nome
    
    
 
    
 
    
 
class Price(models.Model):
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    

    
    