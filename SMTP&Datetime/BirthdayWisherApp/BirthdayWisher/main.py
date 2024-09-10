import random
import smtplib
import os
import datetime as dt
import pandas as pd

MY_EMAIL = "beratyetis5859@gmail.com"
APP_PASSWORD = "weor lryd itkc qgos"
LETTER_DIRECTORY = os.path.join(os.getcwd(), "letter_templates")


def get_letter_files(directory):
    try:
        return [f.strip("'") for f in os.listdir(directory) if f.endswith(".txt")]
    except FileNotFoundError:
        print(f"Cannot Found The Directory: {directory}")
        return []


LETTERS = get_letter_files(LETTER_DIRECTORY)

birthday_data = pd.read_csv("birthdays.csv")
birthdays_dict = {}
for index, row in birthday_data.iterrows():
    key = (row["month"], row["day"])
    if key in birthdays_dict:
        birthdays_dict[key].append((row["name"], row["email"]))
    else:
        birthdays_dict[key] = [(row["name"], row["email"])]

current_date = (dt.datetime.now().month, dt.datetime.now().day)
if current_date in birthdays_dict:
    for person, email in birthdays_dict[current_date]:
        random_letter = random.choice(LETTERS)
        try:
            with open(os.path.join(LETTER_DIRECTORY, random_letter), 'r') as file:
                letter_content = file.read()
                personal_letter = letter_content.replace("[NAME]", person)

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, APP_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: Happy Birthday!\n\n{personal_letter}"
                )
            print(f"Sent!: {email}")

        except FileNotFoundError:
            print(f"Cannot Found Letter: {random_letter}")
        except Exception as e:
            print(f"An Error Occurred: {e}")
