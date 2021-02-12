import requests
from datetime import date, timedelta
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STOCKS API CALL FOR TSLA

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "TC89PV95SEBPZ29O"
}
AV_Endpoint = "https://www.alphavantage.co/query?"

stock_response = requests.get(AV_Endpoint, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()
stock_data = data["Time Series (Daily)"]

# DATE TIME FUNCTION FOR TODAY AND TOMORROW

today = str(date.today() - timedelta(days=1))
yesterday = str(date.today() - timedelta(days=2))
today_stock_price = float(stock_data[today]["4. close"])
yesterday_stock_price = float(stock_data[yesterday]["4. close"])

#  NEWS API CALL FOR TSLA

news_params = {
    "q": COMPANY_NAME,
    "sort": "popularity",
    "apikey": "139bbb4102334dfbac0b955b3d8923a3",
}

NEWS_API = "http://newsapi.org/v2/top-headlines?"

news_response = requests.get(NEWS_API, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
news = {}

for a in range(0, int(news_data["totalResults"])):
    news_data_title = news_data["articles"][a]["title"]
    news_data_description = news_data["articles"][a]["description"]
    news[news_data_title] = news_data_description

# CALCULATING STOCK DIFFERENCE AND CALLING NEWS IF DIFFERENCE MORE THAN 5

stock_difference = round((today_stock_price - yesterday_stock_price), 2)
stock_diff_percent = round((stock_difference / yesterday_stock_price * 100), 2)
stock_icon = ""

if stock_difference > 0:
    stock_icon = "🔺"
elif stock_difference < 0:
    stock_icon = "🔻"

# TWILIO API CALL AND INITIALIZATION WITH ENVIRONMENT VARIABLES

account_sid = os.environ['ACC_SID']
auth_token = os.environ['AUTH_TOKEN']

client = Client(account_sid, auth_token)

if stock_diff_percent < 5:
    for key, value in news.items():
        message = client.messages \
            .create(
            body=f"{STOCK}:{stock_icon}{stock_diff_percent}\n"
                 f"Headline:{key}\n"
                 f"Brief:{value}",
            from_='+18287053749',
            to='+919563419038'
        )
