from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PhoneType(models.Model):
   reviewname = models.CharField(max_length=255)
   phoneproductdescription=models.TextField(null=True, blank=True)


   def __str__(self):
       return self. reviewname
   class Meta:
       db_table ='phoneproducts'

class phoneProduct(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(PhoneType, on_delete=models.CASCADE)  
    dateentered=models.ForeignKey(User, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    productURL=models.URLField()
    phonedescription=models.TextField()

    def __str__(self):
        return self.phonename
 
    class Meta:
        db_table='Phonetype'
        


class Phone(models.Model):
      phonename=models.CharField(max_length=255)
      phoneProduct=models.ForeignKey(phoneproduct, on_delete=models. D0_NOTHING)
      phoneUser=models.ForeignKey(phoneUser, on_delete=models. D0_NOTHING)
      phoneprice=models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
      phonereviewdate=models. DateField()
      phoneurl=models. URLField()
      phoneproductdescription=models.TextField()

      


      def __str__(self):
        return self.phoneproductname


class PhoneReview(models.Model):
      reviewtitle=models.CharField(max_length=255)
      phonereviewdate=models.DateField()
      phoneproduct=ForeignKey(phoneProduct, on_delete=models. D0_NOTHING)
      phoneUser=models.oneTomanyfields(phoneUser, on_delete=models. D0_NOTHING)
      dateentered=models.DateField()
      phonereviewrating=models.smallintergerfield()
      phonereviewtext=models.TextField()


      class Meta:
         db_table= 'phonereviews'



      def __str__(self):
        return self. typename






 
    
   
