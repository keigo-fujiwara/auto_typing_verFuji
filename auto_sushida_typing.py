from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 実行前に
# 1. 仮想環境構築⇒入る
# 2. pip install -r requirements.txt でモジュールをインポート

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome()

# ウィンドウサイズを固定
driver.set_window_size(730, 753)

url = "https://sushida.net/"
driver.get(url)

time.sleep(2)
driver.find_element("xpath", "//a[@href='play.html']").click()

time.sleep(10)

# スタートボタンの座標
start_x = 380
start_y = 360

webgl_element = driver.find_element("xpath", "//*[@id='game']/div")
actions = ActionChains(driver)
actions.move_to_element(webgl_element).perform()

time.sleep(10)

actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, start_x, start_y).click().perform()

time.sleep(3)
