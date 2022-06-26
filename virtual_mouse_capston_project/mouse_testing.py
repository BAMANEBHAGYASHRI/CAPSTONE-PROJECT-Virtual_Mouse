import pyautogui
import mouse
from pynput.keyboard import Key, Controller
import time
import webbrowser
keyboard=Controller()
#text = input("give your command ")
text = "min"
if(text=="min"):
        # minimize keyaaaa
    pyautogui.moveTo(1250, 1)
    time.sleep(2)
    mouse.click('left')
    print("right click")
    pyautogui.moveTo(270, 7)
    mouse.click('left')
    time.sleep(0.2)
    mouse.click('left')
elif(text=="ref"):
                # minimize key
    pyautogui.moveTo(1250, 1)
    time.sleep(2)
    mouse.click('right')
    time.sleep(1)
    pyautogui.moveTo(650, 6)
    time.sleep(2)
    mouse.click('left')
    time.sleep(0.5)
    pyautogui.moveTo(600, 3)
    time.sleep(2)
    mouse.click('left')

elif(text=="down")  :
    for i in range(15):
        keyboard.press(Key.down)
        time.sleep(0.05)
        keyboard.release(Key.down)
        time.sleep(0.05)
elif (text == "chrome"):
    print("chrome")
    webbrowser.open_new_tab("http://www.google.com")

elif (text == "YouTube"):
    webbrowser.open_new_tab("http://www.youtube.com")

