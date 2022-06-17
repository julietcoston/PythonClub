from django import forms
from .models import TechType, TechProduct, Review
from .views import  phonereview, PhoneProduct, PhoneReview
class ProductForm (forms.ModelForm):
    class Meta:
        model=TechProduct
        fields='__all__'

class phoneProductform(form.ModelForm):
    class meta:
        model=phoneProduct
        fields= '__all __'
        