mylist = [1,2,3]
#myString = "My String"

# print(len(mylist))
# print(len(myString))
# print(type(mylist))
# print(type(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie object is created")
    
    def __str__(self):
        return f"{self.title} by {self.duration}"
    
    def __len__(self):
         return self.duration
    
    def __del__(self):
        print("Movie is deleted")
        


m = Movie("Movie name","Director name",120)

# print(str(mylist))
# print(str(m))


# Normally we use the len method with the m object, but if we define the len method ourselves, we can use it as we wish.
# print(len(mylist))
# print(len(m))

del m
# if we delete the object , it is no longer defined
print(m)

