import smtplib
import random
import datetime as dt
import pandas as pd

selected_date = dt.date(year=2024, month=9, day=3)
today = (selected_date.month, selected_date.day)

my_email = "youremail"
my_password = "yourpassword"
birthday_data = pd.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in birthday_data.iterrows()}

file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person.email, msg=f"Subject:Birthday\n\n{contents}")
