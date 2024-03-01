#numbers = [1,3,5,7,9,12,19,21]

# 1-) print numbers to terminal with while loop 

#i = 0
#while(i < len(numbers)):
#    print(numbers[i])
#    i+=1

# 2-) Taking the start and end values ​​from the user as input and printing all odd numbers in between to the terminal
"""
start = int(input("Starting value :   "))
end = int(input("Ending Value :  "))
i = start
while i < end :
    i += 1

    if(i%2!=0):
       print(i)
"""

# 3-) print the numbers from 1 to 100 in decreasing order 
'''
i = 100

while i > 0:
    print(i)
    i-=1

'''
# 4-) print the 5 input values which are taken from user in increasing order 
'''
numbers=[]

i=0
while i<5:
    number = int(input("Enter the value :  "))
    numbers.append(number)
    i+=1
numbers.sort()    
print(numbers)    
'''

# 5-) Store unlimited product information you receive from the user in the product dictionary as (name, price)

products=[]

stockAmount = int(input("How many products you want to stock ? "))
i = 0
while(i < stockAmount):
    i+=1
    name = input("Product name: ")
    price = input("Product price: ")
    products.append({
        "name": name,
        "price":price
    })


for product in products:
    print(f"Procut name {product['name']} , Price : {product['price']}")