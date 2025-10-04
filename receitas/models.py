from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from compras.models import Insumo

class Receita(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    rendimento = models.PositiveSmallIntegerField()
    tempo_preparo_em_minutos = models.PositiveSmallIntegerField()

class Ingrediente(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    unidade_medida_culinaria = models.PositiveSmallIntegerField()
    unidade_medida_sistema_metrico = models.PositiveSmallIntegerField()
    id_receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    id_insumo = models.ForeignKey(Insumo, on_delete=models.RESTRICT)

class Produto(models.Model):    
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    id_receita = models.ForeignKey(Receita, on_delete=models.RESTRICT)