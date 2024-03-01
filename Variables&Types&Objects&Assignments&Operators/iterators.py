# liste = [1,2,3,4,5]

# # normally , if we want to see all members of 'liste' , we can simply use for loop
# for i in liste: # in here , 'liste' is an iterable object
#     print(i)
#-----------------------------------------------------------------------------------------------------------------------------------
# other way 
# iterator = iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#-----------------------------------------------------------------------------------------------------------------------------------

# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

#------------------------------------------------------------------------------------------------------------------------------------


class MyNumber():
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x 
        else:
            raise StopIteration

liste = MyNumber(10,20)

myiter = iter(liste)

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break


# for x in liste :
#     print(x)
