from django.contrib import admin
from .models import Orders,OrderItem




class OrderItemInline(admin.TabularInline):
    model=OrderItem

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
   inlines=[OrderItemInline]
   #list_display=['order_id','user','first_name','last_name','address_line1','address_line2','city','state','Phoneno','created_at','updated_at']
admin.site.register(Orders,OrdersAdmin)
admin.site.register(OrderItem)