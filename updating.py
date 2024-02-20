# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20) 
#     print(file.write("Deneme"))
# we can write something to where we want in file 

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

#--------------- UPDATE ON END OF FİLE -------------------
# with open("newfile.txt","a",encoding="utf-8") as file :
#     file.write("\nFadime Duman")
#appends inside of 'write()' to the end of file
#-----------------------------------------------------------

# -------------- UPDATE ON BEGINNING OF THE FILE -----------

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Turan Duman\n" + content
#     file.seek(0)
#     file.write(content)

#-------------- UPDATE ON MID OF THE FILE --------------------


with open("newfile.txt","r+",encoding="utf-8") as file :
    list = file.readlines()
    list.insert(1,"Talha Duman\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
