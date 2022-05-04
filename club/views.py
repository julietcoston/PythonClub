from django.shortcuts import render
from .models import TechType, Review, TechProduct
# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def products(request):
    product_list=TechProduct.objects.all()
    return render(request, 'club/products.html', {'product_list': product_list})
