from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 35
PROMISED_UP = 10
TWITTER_EMAIL = "email@gmail.com"
TWITTER_PASSWORD = "password"


class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/'
                                                                'div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(50)

        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/'
                                                             'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
                                                              'div[1]/div[1]/div/div[2]/span')

        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/'
                                                              'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/'
                                                              'div/div[2]/span')

        print(self.down.text)
        print(self.up.text)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)

        email = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                            '/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]'
                                                            '/div/input')

        email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                                 'div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        time.sleep(5)
        password_textbox = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/'
                                                                        'div[2]/div[2]/div/div/div[2]/div[2]/div[1]/'
                                                                        'div/div/div[3]/div/label/div/div[2]/div[1]/'
                                                                        'input')
        password_textbox.send_keys(TWITTER_PASSWORD)
        log_in_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/'
                                                                   'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/'
                                                                   'div[1]/div/div/button')
        log_in_button.click()
        time.sleep(5)

        tweet_compose = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                                    'div/div/div/div[3]/div/div[2]/div[1]/div/div/div/'
                                                                    'div[2]/div[1]/div/div/div/div/div/div[2]/div/div/'
                                                                    'div/div/div/div[1]/div/div/div/div/div/div[2]/div/'
                                                                    'div/div/div')

        tweet = (f"Hey @Turkcell Ben 35 Mbit download / 10 Mbit Upload için ödeme yaparken neden internet hızım "
                 f"{self.down} Mbit Donwload / {self.up} Mbit Upload ? ")

        tweet_compose.send_keys(tweet)
        time.sleep(5)

        tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                                   'div/div/div/div[3]/div/div[2]/div[1]/div/div/div/'
                                                                   'div[2]/div[2]/div[2]/div/div/div/button')

        tweet_button.click()
        time.sleep(5)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
