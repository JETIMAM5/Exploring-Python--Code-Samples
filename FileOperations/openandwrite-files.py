# open() function is used for creating files 
# usage is as follows : open(file_name,file_acces_mode)
# file access mode specifies the purpose for which we open the file
#--------------------------------------------------------------------------------------------------------------------
# 'w' = write . Creates file at the directory

# file = open("newfile.txt","w")
# ALTERNATIVE --->> file = open("C:/users/Berat/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Berat Yetiş")
# file.close()
# cursor starts from beginning of the file every time we open it with 'w' access mode , it means previous data will be removed
#-------------------------------------------------------------------------------------------------------------------------------
# 'a' = append . If the file does not exist in the directory it will be created
# The cursor starts after the previously changed position, which means previous changes will not be removed
# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nJETIMAM")
# file.close
#-------------------------------------------------------------------------------------------------------------------------------
#'x' = exclusive creation : if the file already exists , outputs a FileExistsError exception
file = open("newfile2.txt","x",encoding="utf-8")
