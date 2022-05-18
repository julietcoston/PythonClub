from django.test import TestCase
from .models import TechType, product, Review
# Create your tests here.

Class TechTypeTest(TestCase):
 def setup(self):
     self.type=techtype(typename='Lenovo Laptop')
     
 def test_typestring(self):
    self.assertEqual(str(self.type,), 'Lenovo Laptop')