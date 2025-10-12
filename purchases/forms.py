from django import forms
from .models import Supplier, Ingredient, Purchase


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

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase        
        fields = ["date", "supplier", "total"]
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date-local"}),
            "supplier": forms.Select(attrs={"class": "form-select"}),
            "total": forms.NumberInput(attrs={"class": "form-control text-end", "step": "0.01", "min": "0"}),
        }