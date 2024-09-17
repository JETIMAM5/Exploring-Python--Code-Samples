# # def my_decorator(func):
# #     def wrapper(name):
# #         print("Transactions before function")
# #         func(name)
# #         print("Transactions after functon")
# #     return wrapper
#
# # @my_decorator  # --> @function_name = short way to decore a function
# # def sayHello(name):
# #     print("Hello",name)
#
# # sayHello("Ali")
#
#
#
#
# # def greeting():
# #     print("greeting")
#
# # sayHello = my_decorator(sayHello)  #This is the other way of decoring a function
# # sayHello()
# # if I want to do same thing with greeting function
# # greeting = my_decorator(greeting)
# # greeting()
#
# #------------------------------------------------------------------------------------------------------------------------
# import math
# import time
#
# def calculate_time(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         time.sleep(1) # put function to sleep for 1 second
#
#         func(*args,**kwargs)
#
#         finish = time.time()
#         print("Function " + func.__name__ + " is lasted for " + str(finish-start) + " seconds")
#
#     return wrapper
#
# @calculate_time
# def exponentiation(a,b):
#
#     print(math.pow(a,b))
#
# @calculate_time
# def factorial(num):
#
#     print(math.factorial(num))
#
# @calculate_time
# def addition(a,b):
#     print(a+b)
#
#
# exponentiation(2,4)
# factorial(4)
# addition(10,20)


