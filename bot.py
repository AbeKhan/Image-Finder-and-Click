from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# res = pyautogui.locateOnScreen("edit.png") print(res) shake_but =
# print(pyautogui.center(res))

# pyautogui.moveTo(shake_but)


#def click(x, y): #  win32api.SetCursorPos((x, y))
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) #
# time.sleep(0.01) # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,
# 0, 0)

time.sleep(3)   
while True:
    try:
        shake_but = pyautogui.locateOnScreen('shakeText.png', confidence=0.20) #, grayscale=True)
        if shake_but is not None:
            time.sleep(1)
            pyautogui.moveTo(shake_but)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            print(shake_but)
            print("Image Found")
    except pyautogui.ImageNotFoundException:
        print("Image Found not found")
        time.sleep(0.5)
