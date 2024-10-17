from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure a Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using Css selector
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

# Interactions (Auto)
# article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

# Find "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)


# driver.quit()
