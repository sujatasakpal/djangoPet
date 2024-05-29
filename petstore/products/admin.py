from django.contrib import admin
from .models import Product,Category

# Register your models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','product_name','product_description','product_price','product_brand','category']
#Registering product  model on the admin Panel
#admin.site.register(Product,ProductAdmin)method 1 register
#@admin.register(Product) method 2 register
# rgistering category

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']

admin.site.register(Category,CategoryAdmin)