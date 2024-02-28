# from datetime import date
from datetime import datetime
from datetime import timedelta
# from datetime import time
#-------------------------------------------------------------------------------------------------------------------------------------
#import datetime
#-------------------------------------------------------------------------------------------------------------------------------------
# result = datetime.now().year
# result = datetime.now().month
# result = datetime.now().day    
# result = datetime.now().hour 
# result = datetime.now().minute
# result = datetime.now().second  
#-------------------------------------------------------------------------------------------------------------------------------------
noww = datetime.now()  # Current date and time
# An alternative for of 'now' is --> today (they're the same )
# result = datetime.today
# For more accurate time information , we use ctime
#result = datetime.ctime(noww)
#-------------------------------------------------------------------------------------------------------------------------------------
# result = datetime.strftime(noww,"%Y")  # Year
# result = datetime.strftime(noww,"%x")  # Hour:Minute:Second
# result = datetime.strftime(noww,"%d")  # Number of the day
# result = datetime.strftime(noww,"%A")  # Name of the Day -- Day as a string
# result = datetime.strftime(noww,"%B")  # Name of the month -- month as a string
# result = datetime.strftime(noww,"%Y %B %A") # We can use them at the same time
#-------------------------------------------------------------------------------------------------------------------------------------
# t = "28 February 2024 hour 22:27:44"
# day , month , year = t.split()

# print(day)
# print(month)
# print(year)

# we can use an alternative for splitting

# dt = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
#-------------------------------------------------------------------------------------------------------------------------------------
birthday = datetime(2004,1,18,10,00,24)
# result = datetime.timestamp(birthday)  # date to seconds
# result = datetime.fromtimestamp(0)     # 1970.1.1 ( beginning for computers :) )
# result = datetime.fromtimestamp(result) # seconds to date

result = noww - birthday #timedelta object (subtration of two time object)
result = result.seconds  #previous object at seconds form 

result = noww + timedelta(days=10) # sum of two date object --> adds 10 days to today
print(result)

