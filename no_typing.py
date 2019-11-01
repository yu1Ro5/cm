import pythoncom
import pyHook
import time 

def uMad(event):
    return False

print("s")
hm = pyHook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
#s=input()
time.sleep(30)
print("e")
    
    
pythoncom.PumpMessages()