import os
import smtplib
from email.message import EmailMessage

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.com/dp/B0G31647WM"
TARGET_PRICE = 90.00  
MY_EMAIL = os.environ.get("MY_EMAIL")       
MY_PASSWORD = os.environ.get("MY_PASSWORD")   

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

title_tag = soup.select_one("#productTitle")

if title_tag is None:
    print("Amazon blocked the request (no product title found). Try again in a few minutes.")
    exit()

product_title = title_tag.getText().strip()

symbol = soup.select_one(".a-price-symbol").getText()
price_whole = soup.select_one(".a-price-whole").find(string=True, recursive=False).strip().replace(",", "").replace(".", "")
price_decimal = soup.select_one(".a-price-decimal").getText()
price_fraction = soup.select_one(".a-price-fraction").getText()

price = float(f"{price_whole}{price_decimal}{price_fraction}")

print(f"The current price is {symbol}{price}")

# ---- Email ---- #
if price < TARGET_PRICE:
    message = EmailMessage()
    message["Subject"] = "Amazon Price Alert!"
    message["From"] = MY_EMAIL
    message["To"] = MY_EMAIL
    message.set_content(
        f"{product_title}\n\nis now {symbol}{price} (your target: {symbol}{TARGET_PRICE}).\n\n{URL}"
    )

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(message)

    print("Email sent!")