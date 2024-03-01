# def greeting (name):
#     print("hello ",name)

# # print(greeting("Ali")) #Function works and output will be hello Ali
# # print(greeting)        # This will give us to memory address of function


# sayHello = greeting       # Thus , sayHello variable and greeting function become same objects
# # print(sayHello)         # prints memory address of sayHello
# # print(greeting)         # prints memory address of greeting function ,sayHello and this function's

# del sayHello
# print(greeting) # Deleting sayHello doesn't mean that deleting greeting also. Deleting an object do not affect the other object.
#-------------------------------------------------------------------------------------------------------------------------------------------

# ENCAPSULATION
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1+1
#     num2 = inner_increment(num1)
#     print(num1,num2)
    
# outer(10)   # "If the code performing the task resides within the inner function,
# there is no purpose in utilizing the outer function in this manner without invoking the inner function within the scope of the outer function

# If nested functions are to be used, inner functions must be defined (with parameters) within the scope of the outer function.

# inner_increment(10) # An inner function cannot run on its own; instead, it must be called by an outer (external) function. 
#---------------------------------------------------------------------------------------------------------------------------------------------------

def factorial(number):
    # we can check whether the parameter 'number' is an integer or not
    if not isinstance(number,int):
        raise TypeError("Number must be an integer")
    
    # we can also check wheter the parameter 'number' is positive
    if not number >=0:
        raise ValueError("Number must be greater than or equal to 0")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        else:
            return number * inner_factorial(number-1) #RECURSIVE FUNCTION , and that is recursive step
    
    return inner_factorial(number)

try:
    print(factorial("4"))
except Exception as ex:
    print(ex)

      