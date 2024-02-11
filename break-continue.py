#name = "Berat Yetis"
#for letter in name:
#    if(letter =="a"):
#        continue
#    print(letter)

#x = 0
#while x<5:
#   x+=1  
#   if x == 2:
#      continue
#   print(x)

#  EXAMPLE : sum of the odd numbers from 1 to 100 
x = 0
sum = 0
while x <= 100 :
    x+=1
    if(x%2==0):
        continue
    else:
        sum +=x

print(f"Sum of the odd numbers from 1 to 100 is {sum}")