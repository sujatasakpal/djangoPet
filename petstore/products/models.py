from django.db import models
from autoslug import AutoSlugField
# Create your models here.

#-------------------------------------------------------------------
 # creating custom manager (Product)
 #-------------

class CustomProductManager(models.Manager):
    def get_queryset(self) :
        return ProductQuerySet(self.model)
        #return super().get_queryset().order_by('product_name')
      
    def royalcanin(self):
        return super().get_queryset().filter (product_brand="Royal Canin")
    def pawsindia(self):
        return super().get_queryset().filter(product_brand="PawsIndia")
    



    #-----------------------------------

# custom query set(Product) it is optional 

#-------------------

class ProductQuerySet(models.QuerySet):
    def range(self,start_price,end_price):
        return self.filter(product_price__range=(start_price,end_price))
    
    def search (self,keyword):
        return self.filter(product_name__icontains=keyword)
    

#========================================================================================
# category Model
#====================================================================


class Category(models.Model):
    category_name = models.CharField(max_length=50,blank=False)
    category_slug=AutoSlugField(populate_from="category_name",unique=True)

    def __str__(self):
        return self.category_name









#==================================================
  
#(objects)
class Product(models.Model):
    product_name=models.CharField(max_length=70,default="product name")
    product_description=models.TextField(default="Description")
    product_price=models.PositiveIntegerField(default=0)
    product_brand=models.CharField(max_length=50 ,default="superpet")
    product_picture=models.ImageField(upload_to="products/", null=True)
    #ForeignKey helps us to achieve one to many relationship. oNE cATEGORY mANY PRODUCT 
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)

    #changing Manager Name (Product.productManager.all())
    productManager=models.Manager()
    cm=CustomProductManager()
    

    def __str__(self):
        return self.product_name
    



    

