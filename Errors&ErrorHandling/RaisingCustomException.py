# # x = 10 
# # if x>5:
# #     raise Exception("X cannot be bigger than 5...")
#--------------------------------------------------------------------------------------------------------------------------------------
# def check_password(psw):
#     import re
#     if len(psw)<8:
#         raise Exception("Password must contain at least 7 characters...")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Password must contain at least one lowercase [a-z] letter...")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Password must contain at least one uppercase [A-Z] letter...")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Password must contain at least one number [0-9]...")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Password must contain alphanumeric character ( _ , @ or $ )....")
#     elif re.search("\s",psw):
#         raise Exception("Password cannot contain a whitespace...")
#     else:
#         print("Valid Password...")
    
# password = "12345678aA@"
# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Valid password (else)")
# finally:
#     print("Validation is succesful")
#--------------------------------------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self,name,year):
        if len(name)>10:
            print("Name is containing too many characters")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiiiii",1989)
