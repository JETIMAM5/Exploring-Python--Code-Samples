import os
import datetime

result = dir(os) # what's in that module ?
result = os.name # nt = Windows , whats the Operating system of this PC ??

#----------------------------LEARNING THE PATHWAY OF FILE ---------------------------------------------------------

result = os.getcwd() # pathway of this file

#----------------------- FOLDER OPERATIONS ------------------------------------------------------------------------------

#os.mkdir("Newdirectory") # mkdir function creates a new folder on the same pathway 
#os.makedirs("Newdirectory/NewFolder") #Creates nested folder ~ NewFolder is in the Newdirectory 
#os.rename("Newdirectory","NewFolder2") #Changes the name of folder
#os.rmdir("NewDirectory") #rmdir method removes the folder
#os.removedirs("Newdirecorty/NewFolder") #Removes the NewFolder which is in the NewDirectory Folder

#-------------------------------------------------------------------------------------------------------------------

#------------------------------ CHANGING DIRECTORY -------------------------------------------------------------------
#os.chdir("C:\\") # Arranges directory to C:\\ (Pathway)    # ChangeDirectory
#os.chdir("..")  # Used to move to a higher directory
#os.chdir("..//..") Used to move to two level higher directory

#-------------------------------------------------------------------------------------------------------------------
#---------------------------------LISTING OPERATIONS ---------------------------------------------------------------

#result = os.listdir() #Lists all files in the current folder
#result = os.listdir("C:\\") #Lists all files in the C 

# We can also classify or filter the files in a directory and print them like that way :
# for file in os.listdir():
#     if file.endswith(".py"):
#         print(file)
#---------------------------------------------------------------------------------------------------------------------

result  = os.stat("date.py")  # without 'datetime' , that gives us some meaningless information about the file in parameter
#result = result.st_size/1024  # st_size is the size of the file in bytes , if we divide it with 1024 that gives the size in Kilobytes
#result = datetime.datetime.fromtimestamp(result.st_ctime)   # Creating date&time of the file
#result = datetime.datetime.fromtimestamp(result.st_atime)   # Last Access date&time of the file
#result = datetime.datetime.fromtimestamp(result.st_mtime)    # Modifying date&time of the file

#------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------- OPENING AN EXECUTABLE PROGRAM -------------------------------------------------------------

# os.system("notepad.exe")

#----------------------------------------------------------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------- PATH ----------------------------------------------------------------------------
# result = os.path.abspath("_os.py")  # Location (pathway) of a file
# result = os.path.dirname("C:/Users/Berat/OneDrive/Masaüstü/Python/Exploring-Python--Code-Samples/Exploring-Python--Code-Samples/Modules/_os.py") #Directory name of the given Pathway
# result = os.path.dirname(os.path.abspath("_os.py"))
# result = os.path.exists("C:/Users/Berat/OneDrive/Masaüstü/Python/Exploring-Python--Code-Samples/Exploring-Python--Code-Samples/Modules/_os.py")
# result = os.path.isdir("C:/Users/Berat/OneDrive/Masaüstü/Python/Exploring-Python--Code-Samples/Exploring-Python--Code-Samples/Modules/_os.py")
# result = os.path.isfile("C:/Users/Berat/OneDrive/Masaüstü/Python/Exploring-Python--Code-Samples/Exploring-Python--Code-Samples/Modules/_os.py")
# #result = os.path.join("C:/","Deneme") # Joins two  or more directory
# #result = os.path.split("C:/","Deneme") #Split two or more directory
result = os.path.splitext("_os.py") #splits the name of file and extention of file
result = result[0] #it will give us to name of file 
 
print(result)