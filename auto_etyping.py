from selenium import webdriver
import time
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

url = "https://www.e-typing.ne.jp/"
driver.get(url)

time.sleep(1)
driver.find_element("xpath", "//a[@href='./roma/check/']").click()

time.sleep(1)
driver.find_element("id", "level_check_btn").click()

time.sleep(2)
driver.switch_to.frame("typing_content")
driver.find_element("id", "start_btn").click()
time.sleep(2)
body_element = driver.find_element("xpath", '/html/body')

# while True: 無限タイピング用
# 無限ループ時は下記コードのインデントを1つ分ずらす（Tab１回）
body_element.send_keys(" ")
time.sleep(3)
for _ in range(15):
    text = driver.find_element("xpath", "//div[@id='sentenceText']/div/span/following-sibling::span").text
    for char in text:
        body_element.send_keys(char)
    time.sleep(1)

print("===============")
print("Score: ", driver.find_element("xpath", "//*[@id='current']/div[2]/ul/li[1]/div[2]").text)
print("Level: ", driver.find_element("xpath", "//*[@id='current']/div[2]/ul/li[2]/div[2]").text)
print("===============")
    # time.sleep(3)
    # driver.find_element("id", "replay_btn").click() 無限ループ用

input("終了する場合は入力する（何でもOK）：")
# 「Ctrl+C」で終了 無限ループ用（上記のコメントアウトを忘れない）