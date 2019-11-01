from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
import pyautogui as pag
import numpy as np
import random
import pyHook

pag.hotkey('win','d')
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
pag.hotkey('win','t')
pag.hotkey('end')
pag.hotkey('enter')
pag.moveTo(1, 1, duration=0.1)

# ウィンドウの最大化
driver.maximize_window()
driver.get("http://google.co.jp")
pag.PAUSE = 3.0
driver.quit()

def job():
    def uMad(event):
        return False
    
    pag.hotkey('win','d')
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    pag.hotkey('win','t')
    pag.hotkey('end')
    pag.hotkey('enter')
    pag.moveTo(1, 1, duration=0.1)

    # ウィンドウの最大化
    driver.maximize_window()
    driver.get("http://google.co.jp")
    start = time.time()

    while time.time() - start <= 5:
        hm = pyHook.HookManager()
        hm.MouseAll = uMad
        hm.KeyAll = uMad
        hm.HookMouse()
        hm.HookKeyboard()
       
    hm.MouseAll = 0
    hm.KeyAll = 0
    hm.UnhookKeyboard()
    hm.UnhookMouse()
    driver.quit()

# 10分ごとに実行
schedule.every(20).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)