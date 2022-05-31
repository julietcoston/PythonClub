from django.test import TestCase
from .models import TechProduct, TechType, TechReview
from .forms import TechProductForm, TechReviewForm
from datetime import datetime
from django.urls import reverse
from django.urls import.reverse_lazy reverse
# Create your tests here.
# model tests

class TechProductTest(TestCase):
    def test_stringOutput(self):
        techproduct=TechProduct(productname='Lenovo Laptop')
        self.assertEqual(str(techproduct), techproduct.productname)

    def test_tablename(self):
        self.assertEqual(str(TechProduct._meta.db_table), 'techproduct')

class TechTypeTest(TestCase):
    def test_stringOutput(self):
        techtype=TechType(typename='Laptop')
        self.assertEqual(str(techtype), techtype.typename)

    def test_tablename(self):
        self.assertEqual(str(TechType._meta.db_table), 'techtype')

class TechReviewTest(TestCase):
    def test_stringOutput(self):
        techreview=TechReview(reviewtitle='Lenovo Laptop')
        self.assertEqual(str(techreview), techreview.reviewtitle)

    def test_tablename(self):
        self.assertEqual(str(TechReview._meta.db_table), 'techreview')


class TestIndex(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/index.html')

class TestGetProduct(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/reviews/products')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getProducts'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getProducts'))
        self.type=self.client(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/products.html')

class New_Product_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=user.objects.Create_user(usernane='testuser1', password='p@ssw0rd1')
        self.type=TechcType.objects.Create(typename='laptop')
        self.product=product.objects.Create(productname='lenovo', producttype=self.type, user=self.test_user, dateentered=datetime.date (2020,1,10), price=1200.99)

    def test_redirect_if_not logged _in (self):
        response=self.client.get(reverse ('newproduct'))
        self.assertRedirects(response, '/accounts/login/?next=/tech/newproduct/')

    