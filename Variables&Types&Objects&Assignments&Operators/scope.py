#Global Scope
 
# x = "Global x"

# def function():
#     # Local Scope
#     x = "Local x"
#     print(x)

# function()
# print(x)

#Changing a variable in the local scope of a function does not change the value of the variable in the global scope.
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#global
# name = "Berat"

# def changeName(new_name):
#     #local
#     name = new_name
#     print(new_name)

# changeName("Alex")
# print(name)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#name = "global string" # If Both "hello" and "greeting" have not name variable , the name will be "global string" 

# def greeting():
#     #greeting's local scope , hello's global scope 
#     #name = "Alex"

#     def hello():
#         #name = "Ada" #-- hello's local scope , If there is no name variable here, the name will be "Alex". 
#         print("Hello " + name)
    
#     hello()

# greeting()

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# x = 50
# def test():
#     global x
#     print(f"x: {x}") 

#     x= 100
#     print(f"Changed x to {x}")

# test()
# print(x)   

# If x defines as a global in local scope , global x can be modified in local scope