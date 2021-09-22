from django.http.response import HttpResponseBase
from django.shortcuts import render
from django.http import HttpResponse 
from .models import Employee  

# Create your views here.
# def home(request):
#     print("This is my home view function")  
#     return HttpResponse("this is home page and view")
 
def home(request):
    #stu = Employee.objects.all()  
    #stu = Employee.objects.get(pk=1)
    #stu = Employee.objects.order_by("name").first()
    stu = Employee.objects.order_by("name").last()
    return render(request,"enroll/home.html",{"info":stu}) 


