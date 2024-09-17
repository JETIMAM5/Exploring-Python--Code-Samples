#x,y,z = 5,10,20
#x , y = y,x 
#x += 5   #  same as  x = x + 5 
#x -= 5   #  same as  x = x - 5
#x *= 5   #  same as  x = x * 5
#x /= 5   #  same as  x = x / 5
#x %= 5   #  same as  x = x % 5
#y //= 5   #  same as  y = y // 5
#y **= z   #  same as  y = y ** z (there is no obligation to use numbers after assignment operator"=" , we can use variables too.)
#print (x,y,z)

#using assignment operators on tuples , lists , etc... 

values = 1,2,3,4,5
print(values)
print(type(values))
x,y,*z = values
print(x,y,z)
print(x,y,z[0])