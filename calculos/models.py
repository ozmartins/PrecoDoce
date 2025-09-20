from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from receitas.models import Produto
from compras.models import Insumo

class FichaCusto(models.Model):    
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_hora_calculo = models.DateTimeField()
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    id_produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)

class FichaCustoInsumo(models.Model):    
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    id_ficha_custo = models.ForeignKey(FichaCusto, on_delete=models.CASCADE)
    id_insumo = models.ForeignKey(Insumo, on_delete=models.RESTRICT)

class FichaCustoOutrosCustos(models.Model):    
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    unidade_medida_sistema_metrico = models.PositiveSmallIntegerField()
    descricao = models.CharField(max_length=100)
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    id_ficha_custo = models.ForeignKey(FichaCusto, on_delete=models.CASCADE)

class FichaCustoOutrosCustos_Insumo(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_ficha_custo_outros_custos = models.ForeignKey(FichaCustoOutrosCustos, on_delete=models.CASCADE)
    id_insumo = models.ForeignKey(Insumo, on_delete=models.RESTRICT)