# 1- Can user get a driver's licence ? User must 18 or older and has high school or higher level of education
""""
name = input("Enter Your Name Please...\n")
age = int(input("Enter Your Age Please...\n"))
education = input("Enter Your Education Level Please...(High School or University)\n").lower


if (age >= 18):
    if (education=="High School" or "University"):
        print(f"{name} You can get a driver's lisence...")
    else:
        print(f"{name} Your education level is insufficient...")
else:
    print(f"{name} You must be 18 or older...") 
"""
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

# 2-Average grade of a student 
"""
examnote1 = float(input("Enter Your First Exam Grade Please...\n"))
examnote2 = float(input("Enter Your Second Exam Grade Please...\n"))
verbalnote = float(input("Enter Your Verbal Note Please...\n"))

average = (examnote1 + examnote2 + verbalnote)/3

if (average>=0) and (average<25) :
    print(f"Your Average is {average} , your note is F")
elif(average>=25) and (average<45):
    print(f"Your Average is {average} , your note is E")
elif(average>=45) and (average<55):
    print(f"Your Average is {average} , your note is D")
elif(average>=55) and (average<70):
    print(f"Your Average is {average} , your note is C")
elif(average>=70) and (average<85):
    print(f"Your Average is {average} , your note is B")
elif(average>=85) and (average<100):
    print(f"Your Average is {average} , your note is A")                 
else:
    print("Invalid Note...")
"""

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

# 3- Vehicle service time interval (with datetime )calculation
"""
import datetime
date = (input("Since what date has your vehicle been in traffic?(2023/8/9):\n"))
date = date.split("/")

trafficDate = datetime.datetime(int(date[0]),int(date[1]),int(date[2])) 
now = datetime.datetime.now()
InTraffic = now - trafficDate
days = InTraffic.days

if days<=365:
    print("1.Service interval...\n")
elif days > 365 and days <=365*2:
    print("2.Service interval...\n")
elif days > 365*2 and days <=365*3:
    print("3.Service interval...\n")
else:
    print("Invalid time interval...\n")      
"""
