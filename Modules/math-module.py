#***********METHOD 1********************
#import math as process 

#value = dir(math)
#value = help(math)
#value = help(math.cbrt)
#value = math.sqrt(258)
#value = math.ceil(526.7)

#value = process.sin(60)

#print(value)

#***********METHOD 2*********************
# if we define our functiions (with same name in module) , module's function will be used 
#def sqrt(x):
#    print('x : '+ str(x))

from math import factorial,sqrt

# value = factorial(5)

value = sqrt(16)


print(value)