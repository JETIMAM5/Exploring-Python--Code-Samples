# 1-)  range()
#for item in range(50,100,10):
#    print(item)


# 2-) enumerate()

#greeting = "Hello There!"
#for index,letter in enumerate(greeting):
#    print(f"Letter : {letter}  Index : {index} ")


# 3-) zip()

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]

#print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)

