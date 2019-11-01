#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import PIPE, Popen
import os
import sys
app_name="chrome.exe"
def get_current_window_name():
    for i in Popen(['xprop', '-root'],  stdout=PIPE).stdout:
        if '_NET_ACTIVE_WINDOW(WINDOW):' in i:
            for j in Popen(['xprop', '-id', i.split()[4]], stdout=PIPE).stdout:
                if 'WM_ICON_NAME(STRING)' in j:
                    return j.split()[2][1:][:-1]

def toggle_foreground(app_name):
    app = get_current_window_name()
    if not app or not 0 is app.find(app_name):
        os.system('wmctrl -a ' + app_name)
    else:
        os.system('xwit -iconify -names ' + app_name)

if __name__ == '__main__':
    if 2 > len(sys.argv):
        print(u'最前面，最小化の対象にしたいアプリケーションの名前を与えてください．')
    else:
        toggle_foreground(sys.argv[1])