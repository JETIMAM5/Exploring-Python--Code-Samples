# r is the default file access mode, so it doesn't matter whether you type r or not
# the program understands that the modelless open function has r mode
# try:
#    file = open("newfile.txt","r")
# except FileNotFoundError:
#    print("File Not Found!!!")
# finally:
#    print("File is closed...")
#    file.close() 
#--------------------------------------------------------------------------------------------------------------------
file = open("newfile.txt", "r", encoding="utf-8")

# 1st Way to reading datas from file
# for i in file:
    # print(i,end="")
#--------------------------------------------------------------------------------------------------------------------
# # 2nd way --> using read() function
# content1 = file.read()
# print("Content 1")
# print(content1)

# # now cursor standing end of the file so there are no data to read 
# # thus content 2 has no data to read 
# content2 = file.read()
# print("Content 2")
# print(content2)


# #reads 5 bytes
# content = file.read(5)
# #reads 3 bytes
# content = file.read(3)
# print(content)

# file.close()
# #--------------------------------------------------------------------------------------------------------------------

# # 3rd way --> using readline() function 
# readline() reads just 1 line each time 

# print( file.readline(),end="")
# print( file.readline(),end="")
# print( file.readline(),end="")
# print( file.readline(),end="")
#file.close()
# #--------------------------------------------------------------------------------------------------------------------

# # 4th way --> using readlines() function
# list1 = file.readlines()
# print(list1)
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# file.close()
