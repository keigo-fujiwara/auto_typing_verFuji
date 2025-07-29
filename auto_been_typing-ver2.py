from selenium import webdriver
import random, time

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


# 無限タイピング自動＋ランダムセレクト
while True:
    select = random.randint(1, 7)
    time.sleep(1)
    driver.find_element("xpath", f"//input[@value='{select}']/parent::label ").click()

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
    
    time.sleep(2)

    #スクロール前のページの高さを取得
    height = driver.execute_script("return document.body.scrollHeight")

    #スクロール開始位置を設定
    top = 1
    win_height = driver.execute_script("return window.innerHeight")
    #ページ最下部まで、徐々にスクロールしていく
    while top < height:
        top += 5
        driver.execute_script("window.scrollTo(0, %d)" % top)
    time.sleep(3)


    # 難易度選択画面へ（どちらでもOK）
    # driver.find_element("xpath", '/html/body/a/img').click()
    driver.find_element("class name", 'logo').click()

    # driver.quit()