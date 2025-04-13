import requests
import datetime as dt
import smtplib

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

my_lat = 0
my_lng = 0
my_email = "youremail "
my_password = "yourpassword"
if 35 < longitude < 45 and 30 < latitude < 40:
    with smtlib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="toemail", msg=f"Subject:Project\n\nLook up.")

# parameters = {
#     "lat": 0,
#     "lng": 0,
#     "date": "today",
#     "formatted": 0
# }

# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
# print(data["results"]["sunrise"].split("T")[1].split(":")[0])
# time_now = datetime.now()
# print(time_now.hour)
