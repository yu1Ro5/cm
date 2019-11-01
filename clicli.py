import tkinter

# clickイベント
def btn_click():
    print('テスト')

# 画面作成
tki = tkinter.Tk()
tki.geometry('300x200')
tki.title('ボタンイベントの検証')

# ボタン
btn = tkinter.Button(tki, text='計算', command=btn_click)
btn.place(x=140, y=170)