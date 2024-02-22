# def exponentiation(number):
    
#     # In here ; main purpose is returning a function , not a value
#     def inner(power):
#         return number ** power
#     return inner 

# two = exponentiation(2)  #in here ; two references the inner function
# three = exponentiation(3) #in here ; three references the inner function
# print(two(3))              # 3 = inner functions's 'power' parameter
# print(three(4))              # 4 = inner functions's 'power' parameter

#----------------------------------------------------------------------------------------------------------

# def authority_inquiry(page):
#     def inner(role):
#         if role == "Admin":
#             return "Role {0} can acces the page '{1}'".format(role,page)
#         else:
#             return "Role {0} cannot acces the page '{1}'".format(role,page)
#     return inner

# user1 = authority_inquiry("Product Edit")
# print(user1("Admin"))

# user2 =authority_inquiry("Certifications")
# print(user2("Deputy General Manager"))

#----------------------------------------------------------------------------------------------------------
# EXAMPLE : ALTERNATIVE NESTED FUNCTIONS
def process(process_name):
    def addition(*args):
        sum = 0
        for i in args:
            sum += i   
        return sum 
        
    
    def multiplying(*args):
        total = 1
        for i in args:
            total *= i
        return total
    
    if process_name == "addition":
        return addition
    else:
        return multiplying
    
add = process("addition")
print(add(2,3,4,5,6))

multi = process("multiplying")
print(multi(3,5,4))