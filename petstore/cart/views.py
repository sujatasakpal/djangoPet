from django.shortcuts import render,HttpResponseRedirect
from products.models import Product
from .models import Cart,CartItem,Orders,OrderItem  
from .forms import OrderForm
import uuid
import razorpay
from django.views.decorators.csrf import csrf_exempt
from petstore.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def add_to_cart(request,productId):
    # Fetching Product object with the help of id 
    product= Product.productManager.get(id=productId)
    #Fetching current logged in user 
    user=request.user

    cart,created=Cart.objects.get_or_create(user=user)



    cartitem,created =CartItem.objects.get_or_create(cart=cart,products=product)
    quantity=request.GET.get("quantity")
    cartitem.quantity+=int(quantity)
    cartitem.save()
    return HttpResponseRedirect("/products")


#--------------------view Cart-----------------

@login_required(login_url="/login")
def view_cart(request):
   cart,created= Cart.objects.get_or_create(user=request.user)
   cartitems=cart.cartitem_set.all()
   total=0

   request.session["cart_id"]=cart.id

   for cartitem in cartitems:
        total+=cartitem.quantity*cartitem.products.product_price
   return render(request,"cart/cart.html",{"cartitems":cartitems,"total":total})


#-----------------------------------------------------------------------------
# remove cartitem from cart

@login_required(login_url="/login")
def delete_cartitem(request,cartItemId):
    cartitem=CartItem.objects.get(id=cartItemId)
    cartitem.delete()
    return HttpResponseRedirect("/cart")


#----- updating the products in cart----------
@login_required(login_url="/login")
def update_quantity(request,cartItemId):
    cartitem=CartItem.objects.get(id=cartItemId)
    cartitem.quantity=request.GET.get("quantity")
    cartitem.save()
    return HttpResponseRedirect("/cart")



@login_required(login_url="/login")
def checkout(request):
    if request.method=="GET":
        data={"first_name":request.user.first_name,
          "last_name":request.user.last_name}
        form=OrderForm(initial=data)
        return render (request,"cart/checkout.html",{"form":form})

    if request.method=="POST":
        form=OrderForm(request.POST)
        order_id=uuid.uuid4().hex
        if form.is_valid():
            order=Orders.objects.create(order_id=order_id,
                                  user=request.user,
                                  first_name=form.cleaned_data["first_name"],
                                  last_name=form.cleaned_data["last_name"],
                                  address_line1=form.cleaned_data["address_line1"],
                                  address_line2=form.cleaned_data["address_line2"],
                                  city=form.cleaned_data["city"],
                                  state=form.cleaned_data["state"],
                                  Phoneno=form.cleaned_data["Phoneno"])
            
            #cart_id=request.session.get("cart_id")
            cart=Cart.objects.get(pk=request.session.get("cart_id"))
            for cartitem in cart.cartitem_set.all():
                OrderItem.objects.create(order=order,
                                         product=cartitem.products,
                                         quantity=cartitem.quantity)


            return HttpResponseRedirect("/cart/payment/"+order.order_id)


# payment function
@login_required(login_url="/login")
def payment (request,orderId):
    amount=0
    order=Orders.objects.get(order_id=orderId)

    for orderitem in order.orderitem_set.all():
        amount+=orderitem.product.product_price*orderitem.quantity


        

        # razor pay---------------------------------

    client=razorpay.Client(auth=("rzp_test_90XZsRm0uagZda","NszpA7rjim2wrpDpML0dk8Eh"))
    data={"amount":amount*100,"currency":"INR","receipt":orderId}
    payment=client.order.create(data=data)
    print(payment)
    return render(request,"cart/payment.html",{"amount":amount,"payment":payment})

@csrf_exempt 
@login_required(login_url="/login")
def success(request,orderId):
    client=razorpay.Client(auth=("rzp_test_90XZsRm0uagZda","NszpA7rjim2wrpDpML0dk8Eh"))
    check_signature=client.utility.verify_payment_signature({
        "razorpay_order_id":request.POST.get("razorpay_order_id"),
        "razorpay_payment_id":request.POST.get("razorpay_payment_id"),
        "razorpay_signature":request.POST.get("razorpay_signature")
    })
    if check_signature:
         order=Orders.objects.get(pk=orderId)
         order.paid=True
         order.save()
         cart=Cart.objects.get(user=request.user)
         cart.delete()

         send_mail("Order Placed",# subject
                   "Thank you for placing order ",# message
                   EMAIL_HOST_USER,#sender
                   ["priyanka.vibhute@itvedant.com" # receiver
                    ],
                    fail_silently=False
                   )

         return render(request,"cart/success.html")


       



    