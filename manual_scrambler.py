import random
import win32clipboard

#call from clipboard
win32clipboard.OpenClipboard()
textInput = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

casefunc = ("upper", "lower")

#scramble
textoutput = [getattr(i, casefunc[random.randint(0,1)])() for i in textInput]

textoutput = "".join(textoutput)

#paste to clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(textoutput)
win32clipboard.CloseClipboard()