from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://be-engineer.tech/contact')

name_input = driver.find_element("id", "id_username")
name_input.send_keys("beengineer")
