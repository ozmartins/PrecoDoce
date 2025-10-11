from django import forms
from .models import Supplier, Ingredient


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "maxlength": 100})
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "maxlength": 100})            
        }