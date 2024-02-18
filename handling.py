# error handling 
# try:
#    x = int(input("x: "))  
#    y = int(input("y: "))
#    print(x/y)
# except ZeroDivisionError:
#    print("Divisor cannot be 0..")
# except ValueError:
#    print("İnputs must be integer values")
# # we can also evaluate both errors at the same except block
# except (ZeroDivisionError , ValueError) as e:
#   print("Invalid values")
#   print(e)

while True:
  try:
   x = int(input("x : "))
   y = int(input("y : "))
   print(x/y)
  except Exception as ex:
    print("You entered incorrect value --- ",ex)
  else:
     break
  finally:
    print("Try except is over")
  # If except didn't work , else works
