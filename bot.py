from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# res = pyautogui.locateOnScreen("edit.png")
# print(res)
# shake_but = print(pyautogui.center(res))

# pyautogui.moveTo(shake_but)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:
    try:
        shake_but = pyautogui.locateOnScreen('shake2.png', confidence=0.5, grayscale=True)
        if shake_but is not None:
            pyautogui.moveTo(shake_but)
            time.sleep(1)
            #click(int(shake_but.left*2), int(shake_but.top/2))
            pyautogui.click()
            time.sleep(1)
            print(shake_but)
            print("Yes")
    except pyautogui.ImageNotFoundException:
        print("No")
        time.sleep(0.5)
