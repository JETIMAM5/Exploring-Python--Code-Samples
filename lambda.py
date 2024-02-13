numbers = [1,3,5,9,10,4]

#def square(num): return num ** 2 #--> we can write it also like this (just one line)
#square = lambda num : num**2    


# result = list(map(square,numbers)) #--> LAMBDA EXPRESSION 
# print(result)

# Alternative way :

#for item in map(lambda num : num**2,numbers):
#    print(item)

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#def check_even(num):return num%2==0

check_even = lambda num : num%2 ==0

#result = list(filter(check_even,numbers))
#result = list(filter(lambda num: num%2 == 0,numbers)) #With lambda
#result = list(filter(check_even,numbers))

result = check_even(numbers[2])
print(result)