from django.contrib import admin
from .models import produto,Categoria
from django.contrib import admin
from .models import produto, Price
 
 
class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0
 



class ProdutoAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


# Registrar ProdutoAdmin diretamente
admin.site.register(produto, ProdutoAdmin)



admin.site.register(Categoria)