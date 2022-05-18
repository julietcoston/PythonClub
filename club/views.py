from django.shortcuts import render, get_object_or_404
from .models import TechType, Review, TechProduct
from django .urls import reverse_lazy
from .forms import ProductForm
def index(request):
    return render(request, 'club/index.html')

def products(request):
    product_list=TechProduct.objects.all()
    return render(request, 'club/products.html', {'product_list': product_list})



def productDetail(request, id):
    product=get_object_or_404(product, pk=id)
    return render(request, 'tech/productdetail.html', {'product' : product})

def  newProduct(request):
    form=ProductForm

    if request.method== 'post':
        form=ProductForm(request.post)
        if form.isvalid():
            post=form.save(commit=true)
            post.save()
            form=product
            form=ProductForm()
        else:
            form=ProductForm()
            return render(request, 'tech/newproduct.html', {'form':form})
