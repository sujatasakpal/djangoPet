from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate

#home page
#------------------------------
def home(request):
    return render(request,"index.html")


#register page 
def register (request):
    message=None
    if request.method=='GET':

         #form=UserCreationForm()
        form = CustomUserCreationForm()

   

    #print(form)
    if request.method =="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            message="User registration successfull"

        else: 
            message="User Registartion failed"
    return render (request,'register.html',{'form':form,'message':message})







# user login 
#==============================================================

def user_login(request):
    if request.method=="GET":
        return render(request,"login.html")

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
   
    #-------------------------------------
    #---------- using authentication for username and password 

    user=authenticate(username=username,password=password)

    if user is  None:
        message="LogIn Failed"  
        return render(request,"login.html",{"message":message})


    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/products/")
    



#--------------------------------------
#user logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


#demo function for template-filter

def template_filter_example(request):
    data="Hello I am learning Template Filter"
    return render (request,"demo.html",{"data":data})
