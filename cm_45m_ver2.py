from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
import pyautogui
import numpy as np
import random
import pyHook

def uMad(event):
    return False

cm_list = np.zeros(17)
cm_list = [ "https://www.youtube.com/watch?v=MQcMOhMtO_U","https://www.youtube.com/watch?v=pDpUVDYYtYE",
            "https://www.youtube.com/watch?v=YY1yXtCLmjE","https://www.youtube.com/watch?v=dWXAcTKvZlA",
            "https://www.youtube.com/watch?v=_7Xe1dS-tbg","https://www.youtube.com/watch?v=KkzJDg9340s",
            "https://www.youtube.com/watch?v=m3aurHKQOgA","https://www.youtube.com/watch?v=iGG25zI701M",
            "https://www.youtube.com/watch?v=Eo8au83ik7Y","https://www.youtube.com/watch?v=A-LTldDH5_o",
            "https://www.youtube.com/watch?v=71-18kA_G2s","https://www.youtube.com/watch?v=IIjxEns90lY",
            "https://www.youtube.com/watch?v=LbAFFQchpz8","https://www.youtube.com/watch?v=B5QPybgBVB8",
            "https://www.youtube.com/watch?v=B94bCmIBfpU"]

print("cm play")
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
# ウィンドウの最大化
#driver.maximize_window()
print("s")
hm = pyHook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
pyautogui.moveTo(1, 1, duration=1)
driver.get(cm_list[random.randrange(17)])
#検索テキストボックスの要素をId属性名から取得
element = driver.find_element_by_id("movie_player")
#element.send_keys(Keys.SPACE)
element.send_keys("f")
#element.send_keys(Keys.SPACE)
time.sleep(30)
hm.UnhookKeyboard()
hm.UnhookMouse()
print("e")
driver.quit()
#driver.get("http://google.co.jp")

def job():
    print("cm play")
    pyautogui.moveTo(1, 1, duration=1)
    print("s")
    hm.MouseAll = uMad
    hm.KeyAll = uMad
    hm.HookMouse()
    hm.HookKeyboard()
    #driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    # ウィンドウの最大化
    driver.maximize_window()
    driver.get(cm_list[random.randrange(17)])
    #検索テキストボックスの要素をId属性名から取得
    element = driver.find_element_by_id("movie_player")
    #element.send_keys(Keys.SPACE)
    element.send_keys("f")
    #element.send_keys(Keys.SPACE)
    time.sleep(29)
    hm.UnhookKeyboard()
    hm.UnhookMouse()
    print("e")
    driver.quit()
    #driver.get("http://google.co.jp")

# 10分ごとに実行
schedule.every(45).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)