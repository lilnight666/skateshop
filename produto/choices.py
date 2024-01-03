from django.db.models import TextChoices


class choicescategoria(TextChoices):
    shape="shape"
    roda=  "roda"
    rolamento="rolamento"
    amortecedor= "parafuso"
    truck="truck"
    lixa="lixa"
    acessorios="acessorios"
