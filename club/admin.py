from django.contrib import admin
from .models import TechType,TechProduct, Review
# Register your models here.
admin.site.register(TechType)
admin.site.register(TechProduct)
admin.site.register(Review)