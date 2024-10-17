from bs4 import BeautifulSoup
import os
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

header = {
    "Accept-Language": "en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/129.0.0.0 Safari/537.36",
}

URL = "https://appbrewery.github.io/instant_pot/"


def get_product_info(url, header):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    price_with_currency = soup.find("span", class_="a-offscreen").get_text()
    price = float(price_with_currency.split("$")[1])
    product_title = soup.find("span", id="productTitle").get_text().strip()
    return price, product_title


def check_price_and_notify(price, product_title, threshold_price, url):
    if price < threshold_price:
        send_email_notification(product_title, price, url)


def send_email_notification(product_title, price, url):
    message = f"Subject: Amazon Price Alert!!!\n\n{product_title} is on sale for {price}$\n\n{url}!!!!"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("APP_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("EMAIL_ADDRESS"),
            to_addrs=os.getenv("EMAIL_ADDRESS"),
            msg=message.encode("utf-8")
        )
        print("Email sent successfully!")


def main():
    buy_price_threshold = float(os.getenv("BUY_PRICE"))
    price, product_title = get_product_info(URL, header)
    check_price_and_notify(price, product_title, buy_price_threshold, URL)


if __name__ == "__main__":
    main()




