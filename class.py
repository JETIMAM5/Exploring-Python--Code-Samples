# Class

class Person:
    
    #  Class attributes
    address = "No information"


    #  constructor(constrcutor method)
    #  These are object attributes
    def __init__(self,name,year):
        self.name = name
        self.year = year
        print("init worked")

    
    
    # Methods




# Object (Instance)

p1=Person(name="Ali",year=1990) #First way
p2=Person("Berat",2004)         #Second way to define an instance

# Updating 
p1.name = "Salim"
p1.address = "İstanbul"

# Accesing object attributes 
print(f" p1 Name = {p1.name} , Year = {p1.year} , Address = {p1.address}") 
print(f" p2 Name = {p2.name} , Year = {p2.year} , Address = {p2.address}")

print(p1)
print(p2)

#Type of instances will be 'Person' and also they have differenet RAM addresses
print(type(p1))
print(type(p2))

# Instances are not same , because they have different RAM addresses
print(p1==p2)