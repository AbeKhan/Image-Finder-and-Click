import pyautogui

# res = pyautogui.locateOnScreen("edit.png")
# print(res)
# shake_but = print(pyautogui.center(res))

# pyautogui.moveTo(shake_but)

shake_but = pyautogui.locateCenterOnScreen("shake.png", confidence=0.8)
pyautogui.moveTo(shake_but)
pyautogui.click()
pyautogui.sleep(1)
print(shake_but)



