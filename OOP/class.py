# Class
class Person:
    
    #  Class attributes
    address = "No information"


    #  constructor(constrcutor method)
    
    def __init__(self,name,year):

        # object attributes
        self.name = name
        self.year = year
        

    # Instance Method    
    def intro(self):
        print("Hello There . I am "+ self.name)

    # Instance Method  
    def calculateAge(self):
        age = 2024 - self.year
        return age


#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

# Object (Instance)

p1=Person(name="Ali",year=1990) #First way
p2=Person("Berat",2004)         #Second way to define an instance

# Calling method
p1.intro()
print(f"I am {p1.calculateAge()} years old")
p2.intro()
print(f"I am {p2.calculateAge()} years old")
# Updating 
#p1.name = "Salim"
#p1.address = "İstanbul"

# Accesing object attributes 
#print(f" p1 Name = {p1.name} , Year = {p1.year} , Address = {p1.address}") 
#print(f" p2 Name = {p2.name} , Year = {p2.year} , Address = {p2.address}")


#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#print(p2)
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#Type of instances will be 'Person' and also they have differenet RAM addresses
#print(type(p1))
#print(type(p2))
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
# Instances are not same , because they have different RAM addresses
#print(p1==p2)
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------")
class Circle:
    # Class attribute 
    pi = 3.14

    #Constructor
    def __init__(self,radius=1):
        self.radius = radius

    # Instance Method
    def calculate_perimeter(self):
        return (2*(self.pi)*(self.radius))
    
    def calculate_area(self):
        return (self.pi*(self.radius**2))
        
c1 = Circle() # radius = 1
c2 = Circle(3) # radius = 3

print(f"Area of c1 is {c1.calculate_area()} , Periemeter of c1 is {c1.calculate_perimeter()}")
print(f"Area of c2 is {c2.calculate_area()} , Periemeter of c2 is {c2.calculate_perimeter()}")