# Inheritance 

# class Person => name , lastname , age , eat() , run() , drink() .....
# Student(Person) , Teacher(Person) => This way , Student and Teacher classes inherit all attributes and methods of Person class 
# so we don't need to initialize this attributes & methods for Student and Teacher classes 

# class Animal => Dog(Animal) , Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname 
        print("Person is created...")
    
    
    def who_am_i(self):
        print("I am a person..")

    def eat(self):
        print("I am eating...")

class Student(Person): # Student has the all attributes and methods that Person has
    def __init__(self,fname,lname,number):
      Person.__init__(self,fname,lname)
      self.studentNumber = number
      print("Student is created...")
    
    # Method overriding  
    def who_am_i(self):
        print("I am a student")
    
    def sayHello(self):
        print("Hello I am a student ...")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def  who_am_i(self):
        print(f"I am a {self.branch} teacher...")

# Instances of classes
p1 = Person("Ali","Yilmaz")
s1 = Student("Berat","Yetis",1506) 
t1 = Teacher("Ahmet","Yener","Math")

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))
print(t1.firstName + " " + t1.lastName + " " + t1.branch)


# We can use base class's methods with subclass's instance 
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
        