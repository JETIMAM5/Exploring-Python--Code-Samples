# 1 -) Define a function that outputs the received word from user to the terminal a specified number of times
# def write(word,number):
#    print(word*number)

# write("Hello\n",10)

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# 2 -)Define a function that converts an unlimited number of parameters sent to it into a list.

# def convertToList(*args):
#    list1 = []

#    for item in args:
#       list1.append(item)
   
#    return list1
    
# result = convertToList(10,20,30,"Hello","Berat",15.89,'A')
# print(result)

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# 3 -) Find the all prime numbers between the 2 numbers which received from user 


# def findThePrimes(number1,number2):
#     for number in range(number1,number2+1):
#         if number > 1:
#             for i in range(2,number):
#                 if number % i == 0:
#                     break
#             else:
#                 print(number)

# number1 = int(input("Enter Number1 :  "))
# number2 = int(input("Enter Number2 :  "))

# findThePrimes(number1,number2)

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# 4-)Write a function that prints the exact divisors of a number sent to it as a list.

def findExactDivisors(number):
    exactDivisors = []
    for i in range(2,number) :
        if (number % i==0):
            exactDivisors.append(i)
    
    return exactDivisors

print(findExactDivisors(20))