from django import forms
from .models import Fornecedor, Insumo


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "maxlength": 100})
        }


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ["nome"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "maxlength": 100})            
        }