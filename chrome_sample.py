from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pag
import time
import numpy as np
import random
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
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
# ...省略...
# タイムアウト時間を固定するならまとめておく
wait = WebDriverWait(driver, 10)  # Timeout 10秒（最大待ち時間）
print("a")
# 例1: すべて読み込まれて"Google"を含むタイトルが表示されるまで待つ
driver.get('https://www.youtube.com')
print("a")
wait.until(EC.title_contains("YouTube"))
pag.hotkey('win','d')
driver.maximize_window()
driver.get(cm_list[random.randrange(13)])
time.sleep(10)
driver.quit()
print("b")