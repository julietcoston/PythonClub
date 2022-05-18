from django import forms
from .models import TechType, TechProduct, Review

class ProductForm (forms.ModelForm):
    class Meta:
        model=TechProduct
        fields='__all__'

