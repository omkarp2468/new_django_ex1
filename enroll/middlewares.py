# ==========function based middle ware ========

# def my_middleware1(get_response):
#     print("1.Welcome to first time running code")

#     def my_fun(request):
#         print("1.Welcome to the code running before views function")
#         response = get_response(request)

#         print("1.This code will run after the views file")
#         return response

#     return my_fun 

# def my_middleware2(get_response):
#     print("2.Welcome to first time running code")

#     def my_fun(request):
#         print("2.Welcome to the code running before views function")
#         response = get_response(request)

#         print("2.This code will run after the views file")
#         return response

#     return my_fun 

# ========== clas based middel ware ==========
# this is first middleware
from django.http import response

class My_middleware(): 
    def __init__(self,get_response):
        self.get_response=get_response
        print("One time class based middleware running code")
 
    def __call__(self,request):
        print("this will running before class based view function")
        response=self.get_response(request)

        print("this after class based view function")
        return response  

