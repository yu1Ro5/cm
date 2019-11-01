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

cm_list = np.zeros(13)
cm_list = [ "https://www.youtube.com/watch?v=MQcMOhMtO_U",  # SUNTORY Café de BOSS サントリーカフェ・ド・ボス CM
            "https://www.youtube.com/watch?v=dWXAcTKvZlA",  # NISSIN DONBEI 日清食品どん兵衛 CM 「禁断の出会い」篇 30秒
            "https://www.youtube.com/watch?v=_7Xe1dS-tbg",  # 三ツ矢サイダー CM 「やりきろうぜっ KICKBOXING」編 30秒 広瀬すず
            "https://www.youtube.com/watch?v=KkzJDg9340s",  # マウントレーニア WebCM「ほどける瞬間　ヒャダイン」篇 30秒
            "https://www.youtube.com/watch?v=m3aurHKQOgA",  # カロリーメイトCM｜「考えつづける人」篇 30秒
            "https://www.youtube.com/watch?v=iGG25zI701M",  # 明治エッセルスーパーカップSweet's　「フローズンマジック　モンブラン」篇30秒
            "https://www.youtube.com/watch?v=Eo8au83ik7Y",  # Coca-Cola GEORGIA 日本コカ･コーラジョージア CM 「先輩と後輩」篇 30秒
            "https://www.youtube.com/watch?v=A-LTldDH5_o",  # Asahi CALPIS アサヒカルピス CM 「100周年 こどもの日」篇 30秒
            "https://www.youtube.com/watch?v=71-18kA_G2s",  # Coca-Cola GEORGIA 日本コカ･コーラジョージア CM 「花言葉」篇 30秒
            "https://www.youtube.com/watch?v=IIjxEns90lY",  # Coca-Cola ZERO SUGAR 日本コカ･コーラゼロシュガー CM 「Zero Break」篇 30秒
            "https://www.youtube.com/watch?v=LbAFFQchpz8",  # DyDo Blend Coffee GINREI ダイドーブレンドコーヒーギンレイ CM 「人類移住先探索」篇 30秒
            "https://www.youtube.com/watch?v=B5QPybgBVB8",  # Glico Pocky 江崎グリコポッキー CM 「赤い糸」篇 30秒
            "https://www.youtube.com/watch?v=B94bCmIBfpU"]  # Coca-Cola KOCHAKADEN CRAFTEA 日本コカ・コーラ紅茶花伝クラフティー CM 「CRAFTEA PARTY」篇 30秒

# print("cm play")
# driver = webdriver.Chrome("c:/driver/chromedriver.exe")
# ウィンドウの最大化
# driver.maximize_window()
# print("s")
# hm = pyHook.HookManager()
# hm.MouseAll = uMad
# hm.KeyAll = uMad
# hm.HookMouse()
# hm.HookKeyboard()
# pyautogui.moveTo(1, 1, duration=1)
# driver.get(cm_list[random.randrange(13)])
# 検索テキストボックスの要素をId属性名から取得
# element = driver.find_element_by_id("movie_player")
# element.send_keys(Keys.SPACE)
# element.send_keys("f")
# element.send_keys(Keys.SPACE)
# time.sleep(30)
# hm.UnhookKeyboard()
# hm.UnhookMouse()
# print("e")
# driver.quit()
# driver.get("http://google.co.jp")

def job():
    print("cm play")
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    hm = pyHook.HookManager()
    pyautogui.moveTo(1, 1, duration=1)
    print("s")
    hm.MouseAll = uMad
    hm.KeyAll = uMad
    hm.HookMouse()
    hm.HookKeyboard()
    # ウィンドウの最大化
    driver.maximize_window()
    driver.get(cm_list[random.randrange(13)])
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
schedule.every(30).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)