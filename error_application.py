list1 = ["1","2","5a","10b","abc","10","50"]

# 1 -) Find the integer values on the list1 
# for x in list1:
#     try:
#         result =int(x)
#         print(result)
#     except ValueError:
#         continue
#--------------------------------------------------------------------

# 2 -) Check whether the input is an integer , except 'q' character (q = quit)
# while True:
#     number = input("Number: ")
#     if  number == 'q':
#         break
#     try:
#         result = float(number)
#         print("Number you entered is ", result)
#         break
#     except ValueError:
#         print("Invalid Number")
#         continue
#------------------------------------------------------------------------

# 3 -)Give user Turkish character error for password

# def check_password(password):
#     Turkish_characters = "üöçşİığ"
#     for char in password:
#        if char in Turkish_characters:
#         raise TypeError("Turkish character error!!")
#        else:
#         pass
#     print("Valid password")

# password = input("Password : ")
# try:
#   check_password(password)
# except TypeError as err:
#   print(err)
#------------------------------------------------------------------------

# 4 -) Create a factorial function and write error messages about it 
def factorial(x):
    x = int(x)
    if x < 0:
        raise ValueError("A negative number has no factorial...")
    
    result = 1

    for i in range(1,x+1):
        result *= i
    return result

for x in [5,10,20,"3a",-10]:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
  

