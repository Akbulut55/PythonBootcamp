import smtplib

# my_email = "youremail"
# my_password = "yourpassword"
#
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="toemail",
#     msg="Subject:hello\n\nThis is the body of my email"
#     )
# connection.close()

# alternative connection
# with smtlib.SMTP("smtp.gmail.com", port=587) as connection:


import datetime as dt
import random
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(now)
# print(year)
# print(day_of_week)
# if year == 2024:
#     print("year is 2024")
# date_of_birth = dt.datetime(year=2003, month=9, day=3)
# print(date_of_birth)

current_date = dt.datetime.now()
current_day = current_date.weekday()
if current_day == 2:
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.read().splitlines()
        random_quote = random.choice(quote_list)

    my_email = "youremail"
    my_password = "yourpassword"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="toemail",
            msg=f"Subject:Quote of The Day\n\n{random_quote}"
        )
