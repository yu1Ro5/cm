from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
import pyautogui as pag
import numpy as np
import random
import pyHook


driver = webdriver.Chrome("c:/driver/chromedriver.exe")
pag.hotkey('win','t')
pag.hotkey('end')
pag.hotkey('enter')
pag.moveTo(1, 1, duration=1)

# ウィンドウの最大化
driver.maximize_window()
driver.get("http://google.co.jp")
pag.PAUSE = 3.0
driver.quit()