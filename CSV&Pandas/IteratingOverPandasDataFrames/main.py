import pandas as pd

student_dictionary = {
    "student": ["Mathilda", "Adam", "Sue"],
    "scores": [89, 78, 100]
}

student_data_frame = pd.DataFrame(student_dictionary)
print(student_data_frame)

# Loop through a DataFrame
for (key, value) in student_data_frame.items():
    print(value)  # This going to give us each student's score
    # Means loops through each of the columns

# But this is not usable in every case , that's why we need Pandas in-built loop for DataFrames

# Loop through rows of a DataFrame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    if row.student == "Mathilda":
        print(row.scores)

