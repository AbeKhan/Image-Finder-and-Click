from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    try:
        
        if pyautogui.locateOnScreen('shake.png', confidence=.175) is not None:
            print("Yes")
            time.sleep(0.5)
    except pyautogui.ImageNotFoundException:
            print("No")
            time.sleep(0.5)
