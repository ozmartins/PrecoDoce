from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class Fornecedor(models.Model):    
    nome = models.CharField(max_length=100)

class Insumo(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ultimo_custo = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])

class Compra(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.RESTRICT)

class CompraItem(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    unidade_medida_sistema_metrico = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    id_insumo = models.ForeignKey(Insumo, on_delete=models.RESTRICT)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

class FichaKardex(models.Model):    
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_insumo = models.ForeignKey(Insumo, on_delete=models.RESTRICT)
    data = models.DateTimeField()
    tipo_movimento = models.PositiveSmallIntegerField()
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    quantidade_final = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    valor_final = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])