import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_price = "https://www.alphavantage.co/query?"
price_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "yourapi"
}
price_response = requests.get(stock_price, params=price_param)
price_data = price_response.json()["Time Series (Daily)"]
price_data_list = [value for (key, value) in price_data.items()]
yesterday_data = price_data_list[0]["4. close"]
day_before_yesterday_data = price_data_list[1]["4. close"]
difference = ((float(yesterday_data) - float(day_before_yesterday_data)) / float(day_before_yesterday_data)) * 100
if difference < 0:
    difference_symbol = "🔻"
elif difference > 0:
    difference_symbol = "🔺"
else:
    difference_symbol = "➖"
difference = abs(difference)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

stock_news = "https://newsapi.org/v2/everything?"
news_param = {
    "q": COMPANY_NAME,
    "pagesize": 3,
    "apiKey": "eacfaa0fd4aa49cca25b0204b3b2cb41"
}
news_response = requests.get(stock_news, params=news_param)
news_data = news_response.json()
articles = []
for x in range(0, 3):
    article = {title: description for (title, description) in news_data["articles"][x].items()
               if title == "title" or title == "description"}
    articles.append(article)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
for x in range(0, 3):
    print(f"{STOCK}: {difference_symbol}{difference:.2f}%")
    print("Headline: ", end="")
    print(articles[x]["title"])
    print("Brief: ", end="")
    print(articles[x]["description"])

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
