import pyHook
import time

def uMad(event):
    return False

time.sleep(5)
print("s")
hm = pyHook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
print("m")
time.sleep(20)
hm.UnhookMouse()
hm.HookKeyboard()
print("e")