def sayHello(name = "User"):
    return "Hello "+name

sayHello("Berat")
sayHello()

msg = sayHello("Esma")
print(msg)

def total(num1,num2):
    return num1+num2

sum = total(2,9)
print(sum)

def ageCalculator(dateOfBirth):
    return 2024 - dateOfBirth

BeratsAge = ageCalculator(2004)
EsmasAge = ageCalculator(2013)
print(BeratsAge,EsmasAge)

def retirementCalculator(dateOfBirth,name):

    """
    DOCSTRING : This function calculates how many years left until somebodys's retirement .... 
    INPUT     : Date of birth , name 
    OUTPUT    : Information on the remaining years until retirement.
    """
    age = ageCalculator(dateOfBirth)
    retirement = 65-age

    if retirement > 0:
        print(f"{retirement} years left until your retirement...")
    else:
        print("You're already retired...")    

BeratRetirement = retirementCalculator(2004,"Berat")
print(BeratRetirement)        

print(help(retirementCalculator))