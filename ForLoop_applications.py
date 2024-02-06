numbers=[1,3,5,7,9,12,19,21]

# 1-Which numbers are divisible by 3 from the list 'numbers'?
#for number in numbers:
#    if (number % 3 == 0):
#        print(number)

# 2-Whats the sum of the numbers ? 
#sum = 0
#for num in numbers:
#    sum += num
#print(sum)

# 3-Whats the square of odd numbers from the list 'numbers'?
#for num in numbers:
#    if(num %2 != 0):
#        print(num**2)

#------------------------------------------------------------------------------------------------

cities = ["İstanbul","Ankara","İzmir","Sivas","Erzurum"]

# 4-Which city names from the list 'cities' are consist of  maximum 5 character ?

#for city in cities:
#    if (len(city)<=5):
#        print(city)

#------------------------------------------------------------------------------------------------

products = [
    {"Name":"IPhone 12 Pro" , "Price":"999"},
    {"Name":"IPhone 13 Pro" , "Price":"1099"},
    {"Name":"IPhone 14 Pro" , "Price":"1199"},
    {"Name":"IPhone 15 Pro" , "Price":"1299"}
 
]

# 5-Whats the sum of Prices ?
#sum = 0
#for phone in products :
#    price = int(phone["Price"])  
#    sum += price 
#print(sum)      

# 6-Which Products have a maximum price of 1100? 
for phone in products:
    if(int(phone["Price"])<=1100):
        print(phone["Name"])    