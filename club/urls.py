from django.urls import path 
from .models import views
from django.urls import reverse

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('productDetail/<int:id>', views.productDetail, name='detail'),
    path('newproduct/', views.newProduct, name='newproduct'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path(' phonereview/', views. phonereview,name='phonereview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name= 'logoutmessage'),
    
]

from django.contrib import admin
from django.urls import include, path


urlpatterns= [
    path('polls/', include('polls.url')),
    path( 'admin/', admin.siteurls),
    path('accounts/', include('django.contrib.auth.urls'))
]