from django.test import TestCase
from.models import Product

# Create your tests here.
class ProductTest(TestCase):
    def test_all_users(self):
        products=Product.productManager.all()
        self.assertTrue(len(products)>0)

    
