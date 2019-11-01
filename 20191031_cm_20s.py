from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pag
import time
import numpy as np
import random
import schedule
import datetime
import logging
import datetime
print(datetime.datetime.now())
# ログの出力名を設定
logger = logging.getLogger('LoggingTest')
 
# ログレベルの設定
logger.setLevel(10)
 
# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)
 
# ログのファイル出力先を設定
fh = logging.FileHandler('test.log')
logger.addHandler(fh)
 
# ログの出力形式の設定
formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

def check():
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get('http://abehiroshi.la.coocan.jp/')
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    driver.quit()
check()

def job():
    #print(datetime.datetime.now())
    logger.log(20, 'CM start')
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.minimize_window()
    driver.get("https://www.youtube.com/watch?v=o5Z-DWwSrMY")
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    pag.hotkey('win','d')
    driver.find_element_by_id("movie_player").send_keys("f")
    pag.hotkey('win','t')
    pag.hotkey('end')
    pag.hotkey('enter')
    player_status = 1
    while True:
            player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
            if player_status == 0:
                break
    driver.quit()
    #print(datetime.datetime.now())
    logger.log(20, 'CM end')

schedule.every(20).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)