import subprocess
import time
import win32gui
import win32process
import win32api

MOUSEEVENTF_LEFTDOWN = 0x2
MOUSEEVENTF_LEFTUP = 0x4

def main():
    # メモ帳の起動
    subprocess.Popen(r'notepad.exe')

    # 起動するまで待機
    time.sleep(1)

    # 起動したメモ帳のハンドルを取得する。
    hw1 = win32gui.GetForegroundWindow()
    print(hw1)
    tid1 = win32process.GetWindowThreadProcessId(hw1)

    # ウェイトして他プロセスをアクティブにしておく。
    time.sleep(10)

    # アクティブにした他プロセスのハンドルを取得する。
    hw2 = win32gui.GetForegroundWindow()
    print(hw2)
    tid2 = win32process.GetWindowThreadProcessId(hw2)

    # トップレベルウィンドウを切り替える（この時点ではフォーカスできていない）
    win32process.AttachThreadInput(tid1, tid2, True)
    win32gui.BringWindowToTop(hw1)
    win32process.AttachThreadInput(tid1, tid2, False)

    # ウィンドウの左上の隅っこをクリックしてアクティブにする。
    (left, top, right, bottom) = win32gui.GetWindowRect(hw1)
    print(left, top, right, bottom)
    win32api.SetCursorPos((left + 1, top + 1))
    time.sleep(0.1)
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

if __name__ == '__main__':
    main()