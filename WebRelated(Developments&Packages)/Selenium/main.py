from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#-----------------------------------------------AMAZON-----------------------------------------------------------------
# driver.get("https://www.amazon.com/dp/B0C4FVBNGT/ref=sspa_dk_detail_1?pd_rd_i=B0C4FVBNGT&pd_rd_w=zNIJk&content-id=amzn1."
#            "sym.f2f1cf8f-cab4-44dc-82ba-0ca811fb90cc&pf_rd_p=f2f1cf8f-cab4-44dc-82ba-0ca811fb90cc&pf_rd_r="
#            "E2890JCVHM1JWCH9WCB7&pd_rd_wg=b5NJq&pd_rd_r=56322d7c-1a64-4fb0-adec-9582d4936dbf&s=kitchen&sp_csd="
#            "d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1")
# # ByPassing the captcha
# captcha = driver.find_element(By.LINK_TEXT, "Try different image")
# captcha.click()
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cent.text}$")

#---------------------------------------------- PYTHON -----------------------------------------------------------------
# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")   ##finding by NAME
# # print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID,  value="submit")  ## finding by ID
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")  # Finding by CSS Selecetor
#                                                                     # (For ones don't have any id, name,class or else)
# print(documentation_link.text)
#
# # We can also use the XPath(right click-inspect- rc -Copy XPath) for ones don't have any spesific name, id, class ...
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# # driver.close()  # Closes single tab
# driver.quit()   # Closes whole browser

driver.get("https://www.python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {i+1: {"time": event_times[i].text, "name": event_names[i].text} for i in range(len(event_times))}
print(events)

driver.quit()
