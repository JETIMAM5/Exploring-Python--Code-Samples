numbers = [1,10,5,16,4,9,10]
letters= ["a","g","s","b","y","a","s"]

val  = min(numbers)
val1 = max(numbers)
val2 = min(letters)
val3 = max(letters) 
val4 = numbers[3:6]
val5 = numbers[:4]

print(val)
print(val1)
print(val2)
print(val3)
print(val4)
print(val5)
numbers[4]= 0
numbers.append(40)
numbers.insert(3,78)
numbers.insert(-1,58)
numbers.pop(-1)
numbers.remove(1)
numbers.sort()
letters.sort()
numbers.reverse()
letters.reverse()
print(numbers)
print(letters)
print(numbers.count(10))
print(letters.count("a"))