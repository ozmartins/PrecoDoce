from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from recipes.models import Product
from purchases.models import Ingredient

class RecipeCostSheet(models.Model):    
    calc_date_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)

class RecipeCostSheetIngredient(models.Model):    
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    recipe_cost_sheet_id = models.ForeignKey(RecipeCostSheet, on_delete=models.CASCADE)
    Ingredient_id = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)

class RecipeCostSheetOtherCosts(models.Model):    
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    metrix_system_unit = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=100)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    recipe_cost_sheet_id = models.ForeignKey(RecipeCostSheet, on_delete=models.CASCADE)

class RecipeCostSheetOtherCostsIngredient(models.Model):
    recipe_cost_sheet_other_costs_id = models.ForeignKey(RecipeCostSheetOtherCosts, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)