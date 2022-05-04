from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class TechType(models.Model):
    typename = models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255)


    def __str__(self):
        return self.typename
 
    class Meta:
        db_table='techtype'
   
class TechProduct(models.Model):
    productname=models.CharField(max_length=255)
    techtype=models.ForeignKey(TechType, on_delete=models.CASCADE)  
    dateentered=models.ForeignKey(User, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    productURL=models.URLField()
    productdescription=models.TextField()

    def __str__(self):
        return self.productname
 
    class Meta:
        db_table='techproduct'

class Review(models.Model): 
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(TechProduct, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.title

    class meta:
        db_table= 'review'