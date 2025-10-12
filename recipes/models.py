from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from purchases.models import Ingredient

class Recipe(models.Model):
    #tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)    
    preparation_time_minutes = models.PositiveSmallIntegerField()

class Ingredient(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    imperial_system_unit = models.PositiveSmallIntegerField()
    metric_system_unit = models.PositiveSmallIntegerField()
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)

class Product(models.Model):    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    recipe = models.ForeignKey(Recipe, on_delete=models.RESTRICT)
    recipe_yeld = models.PositiveSmallIntegerField()
    recipe_yeld_unit = models.PositiveSmallIntegerField()