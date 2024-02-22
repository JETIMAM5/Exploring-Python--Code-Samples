def calculate_grade(row):
    row = row[:-1]
    liste = row.split(":") 
    studentName = liste[0]
    grades = liste[1].split(",")

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    average = ( grade1 + grade2 + grade3 ) / 3

    if average >= 90 and average <= 100 :
        letter = "AA"
    elif average >= 85 and average <=89:
        letter = "BA"
    elif average >= 80 and average <=84:
        letter = "BB"
    elif average >= 75 and average <=79:
        letter = "CB"
    elif average >= 70 and average <= 74:
        letter = "CC"
    elif average >= 65 and average <= 69:
        letter = "DC"
    elif average >= 60 and average <= 64:
        letter = "DD"
    else :
        letter = "FF"

    return studentName + " " + letter + "\n"

    


def read_averages():
    with open("exam_grades.txt","r",encoding="utf-8") as file:
       for row in file:
           print(calculate_grade(row))
def grade_entry():
    name = input("Student Name: ")
    lastname = input("Student Lastname: ")
    grade1 = input("Grade 1: ")
    grade2 = input("Grade 2: ")
    grade3 = input("Grdae 3: ")
    with open("exam_grades.txt","a",encoding="utf-8") as file:
        file.write(name+' '+lastname+': '+grade1+','+grade2+','+grade3+'\n')

def save_notes():
    with open("exam_grades.txt","r",encoding="utf-8") as file :
        liste = []

        for i in file :
            liste.append(calculate_grade(i))
    
    with open ("results.txt","w",encoding="utf-8") as file2:
        for i in liste :
            file2.write(i)



while True:
    procces = input("1 - Read the grades\n2 - Enter a grade\n3 - Save the grades\n4 - Exit\n")

    if procces == "1":
        read_averages()
    elif procces == "2":
        grade_entry()
    elif procces == "3":
        save_notes()
    else:
        break