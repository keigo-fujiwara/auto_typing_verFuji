from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://typing.be-engineer.tech"
driver.get(url)

time.sleep(1)
driver.find_element("id", "id_username").send_keys("K5")

time.sleep(1)
driver.find_element("id", "id_password").send_keys("thisistest")

time.sleep(1)
driver.find_element("class name", "login__btn").click()

time.sleep(1)
driver.find_element("xpath", "//input[@value='timeattack']/parent::label ").click()

time.sleep(2)
driver.find_element("xpath", "//input[@value='5']/parent::label ").click()

time.sleep(1)
driver.find_element("class name", "submit__btn").click()

time.sleep(1)
target_xpath = '/html/body'
body_element = driver.find_element("xpath", target_xpath)
body_element.send_keys(" ")


time.sleep(3)
for _ in range(20):
    text = driver.find_element("id", "untyped").text
    for char in text:
        body_element.send_keys(char)

driver.quit()