import random 

#result = dir(random)
#result = help(random) 
#result = random.random() # 0.0 - 1.0
#result = random.random() * 100
#result = int(random.uniform(10,100))
#result = random.randint(1,100)

greeting = "Hello There!"
names =["Ali","Yağmur","Cengiz","Kurt"]

#result = names[random.randint(0,len(names)-1)]
#result = random.choice(names)
#result = random.choice(greeting)

#list1 = list(range(10))
#random.shuffle(list1)
#result = list1

#list2 = range(100)
#result = random.sample(list2,3)

result = random.sample(names,2)

print(result)