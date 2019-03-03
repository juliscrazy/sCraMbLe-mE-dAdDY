import win32api, win32con
import random
import time
import win32clipboard

ctrl = 0xA2
a = 0x41
v = 0x56
x = 0x58
alt = 0x12
tab = 0x09

win32clipboard.OpenClipboard()
try:
    oldclipboard = win32clipboard.GetClipboardData()
except TypeError:
    oldclipboard = "None"
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()

win32api.keybd_event(alt, 0, 0, 0)
win32api.keybd_event(tab, 0, 0, 0)
win32api.keybd_event(tab,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(alt,0 ,win32con.KEYEVENTF_KEYUP ,0)

time.sleep(0.1)

#select all
win32api.keybd_event(ctrl, 0, 0, 0)
win32api.keybd_event(a, 0, 0, 0)
time.sleep(0.1)
win32api.keybd_event(a,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(ctrl,0 ,win32con.KEYEVENTF_KEYUP ,0)


time.sleep(0.1)

#copy
win32api.keybd_event(ctrl, 0, 0, 0)
win32api.keybd_event(x, 0, 0, 0)
time.sleep(0.1)
win32api.keybd_event(x,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(ctrl,0 ,win32con.KEYEVENTF_KEYUP ,0)


time.sleep(0.1)

#call from clipboard
win32clipboard.OpenClipboard()
textInput = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

textInput = list(textInput)
textoutput = []
i = 0

#scramble
for letter in textInput:
    x = random.randint(0,1)
    print(x)
    if x == 1:
        var = letter.upper()
    else:
        var = letter.lower()
    textoutput.append(var)
    
textoutput = "".join(textoutput)

#paste to clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(textoutput)
win32clipboard.CloseClipboard()

#paste from clipboard
win32api.keybd_event(ctrl, 0, 0, 0)
win32api.keybd_event(v, 0, 0, 0)
win32api.keybd_event(v,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(ctrl,0 ,win32con.KEYEVENTF_KEYUP ,0)

time.sleep(0.1)

#restore clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(oldclipboard)
win32clipboard.CloseClipboard()

input()