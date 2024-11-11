
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdhyMiyJ6igrsROrHeYc0dL-aZEIk5Jr59KB4ANsMABOQtFTA/viewform?usp=sf_link"
WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(WEBSITE_URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

all_property_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_property_links = [link["href"] for link in all_property_elements]

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]

all_address_elements = soup.select(".StyledPropertyCardDataArea-anchor address")
all_addresses = [address.get_text().replace("|", "").strip() for address in all_address_elements]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_property_links)):
    driver.get(FORM_URL)
    time.sleep(5)

    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div')

    price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div')

    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div')

    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_property_links[n])
    submit_button.click()




