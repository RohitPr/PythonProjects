import smtplib
import requests
from bs4 import BeautifulSoup

MY_EMAIL = "email"
MY_PASSWORD = "pass"

amazon_link = "https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5T31M6/ref=sr_1_3?crid=2J8XHQYKXC6GK&dchild=1"
user_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
}

response = requests.get(url=amazon_link, headers=user_headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "lxml")
amazon_data = soup.find(name="span", id="priceblock_ourprice")
amazon_price = (amazon_data.getText().replace("\xa0", " ")).split("₹")[1]
price = float(amazon_price.replace(",", ""))
base_price = 200000

if price < base_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:iPhone Price Drop \n\nGood News!\n\nThe iPhone is Cheaper than Usual. Check Now:{amazon_link}",
        )
