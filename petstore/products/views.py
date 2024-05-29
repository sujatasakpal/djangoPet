from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,Category
from  django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
class ProductView(ListView):
    model=Product
    # template_name- html file
    #context_object_name

class ProductDetailView(DetailView):
    model=Product
    template_name="products/product_detail.html"
    context_object_name="product"

def royalCanin(request):
    royalCaninProducts=Product.cm.royalcanin()
    return render(request,"products/royalcanin.html",{"royal_canin":royalCaninProducts})

# search functionality 

#------------

def search_products(request):
    keyword=request.GET.get("keyword")
    products=Product.cm.all().search(keyword)
    return render(request,"products/search.html",{"products":products})

#---------------------------------------------------
# Detail View for Category

class CategoryDetailView(DetailView):
    model=Category
    template_name="category/category.html"
    context_object_name="category"
    slug_field="category_slug"
    slug_url_kwarg="slug"

 # create Product

class ProductCreateView(CreateView):
    model=Product
    fields="__all__"
    success_url="/create-product"

class ProductUpdateView(UpdateView):
    model=Product
    fields="__all__"
    success_url="/admin"

class ProductDeleteView(DeleteView):
    model=Product
    success_url="/admin"

class ProductAdminView(ListView):
    model=Product
    template_name="products/productadmin.html"
    #object_list
    
