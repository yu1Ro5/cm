import subprocess
import time
import win32gui
import win32process
import win32api

VK_TAB = 0x09
VK_SHIFT = 0x10
VK_MENU = 0x12
KEYEVENTF_KEYUP = 0x2

def main():
    # メモ帳の起動
    p = subprocess.Popen(r'notepad.exe')

    # 起動するまで待機
    time.sleep(1)

    # 起動したメモ帳のハンドルを取得する。
    hw1 = win32gui.GetForegroundWindow()
    print(hw1)

    # ウェイトして他プロセスをアクティブにしておく。
    time.sleep(10)

    while p.poll() is None:
        # 現在アクティブなウィンドウと一致していれば終了
        hw2 = win32gui.GetForegroundWindow()
        print(hw2)
        if hw1 == hw2:
            break
        time.sleep(1)

        # 現在アクティブでなければ、Alt + Shift + Tab を送信する。
        win32api.keybd_event(VK_MENU, 0, 0)
        win32api.keybd_event(VK_SHIFT, 0, 0)
        win32api.keybd_event(VK_TAB, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(VK_TAB, 0, KEYEVENTF_KEYUP)
        win32api.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP)
        win32api.keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP)
        time.sleep(0.1)

if __name__ == '__main__':
    main()