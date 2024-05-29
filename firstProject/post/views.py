from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
def employee(request):
    employees={
        "101":{"name":"manoj","age":25,"salary":50000},
        "102":{"name":"Nisha","age":29,"salary":40000}

    }
    return render(request,"employee.html",{"employees":employees})

def students(request):
    students={
        "1":{"name":"Shweta","age":10,"class":5},
        "2" :{"name":"Janki","age":12,"class":6}
    }
    return render (request,"students.html",{"students":students})

def subjects(request):
    return render (request,"subject.html",{"subject":["Maths","English","History","Science"]})

def inputData(request):
    return render (request,"data.html")

# def submit(request):
   # username=request.GET.get("Username")
   # print(username)
   # return render (request,"data.html",{"username": username})

def submit(request):
    if request.method=="GET":
        return HttpResponse("you are not allowed to be here through get")
    elif request.method =="POST":
        username= request.POST.get("Username")
        phoneno = request.POST.get("phoneno")
        print(username)
        return render (request,"data.html",{"username": username,"phoneno":phoneno})


# Create your class based View 
class MyView(View):
        def get (self,request):
            #return HttpResponse("<h1>First Class Based View</h1>")
             return render(request,"myview.html")
        def post (self,request):
             username=request.POST.get("username")
             city=request.POST.get("city")
             number=request.POST.get("number")
             return render(request,"myview.html",{"username":username,"city":city, "number":number})
#===========================================
#Template View
class StudentView(TemplateView):
     template_name="studentview.html"
     def get_context_data(self):
            #to call parent constructor we have to use super
            context = super().get_context_data()
            context["name"]="Janki"
            context["age"]=18
            return context
         

                   
            
            
