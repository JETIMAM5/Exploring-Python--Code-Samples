from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure a Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value='fname')
last_name = driver.find_element(By.NAME, value='lname')
e_mail = driver.find_element(By.NAME, value='email')


first_name.send_keys('Adam')
last_name.send_keys('Len')
e_mail.send_keys('dummy@gmail.com')


submit = driver.find_element(By.CSS_SELECTOR, value='form button')
submit.click()