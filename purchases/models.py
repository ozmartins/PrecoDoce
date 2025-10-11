from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Supplier(models.Model):    
    name = models.CharField(max_length=100)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    #last_cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])


class Purchase(models.Model):
    date_time = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    supplier_id = models.ForeignKey(Supplier, on_delete=models.RESTRICT)


class PurchaseItem(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    metric_system_unit = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    purchase_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)


class InventoryLedger(models.Model):    
    Ingredient_id = models.ForeignKey(Purchase, on_delete=models.RESTRICT)
    date = models.DateTimeField()
    movement_type = models.PositiveSmallIntegerField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    cumulative_quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    cumulative_cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])