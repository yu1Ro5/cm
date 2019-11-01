# -*- coding:utf-8 -*-
import subprocess

# タスクマネージャーのプロセスを取得
proc = subprocess.Popen('tasklist', shell=True, stdout=subprocess.PIPE)

# 1行ずつ表示
for line in proc.stdout:
    print(line.decode('shift-jis'))