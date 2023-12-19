# How to use buttons and keyboard shortcuts
import pyautogui
from time import sleep

pyautogui.click(1411, 265, duration=2)
sleep(1)

pyautogui.typewrite('admin@hotmail.com')
sleep(1)

pyautogui.press('tab')
sleep(1)

pyautogui.typewrite('123456')
sleep(1)

pyautogui.press('tab')
sleep(1)

pyautogui.press('space')

# to check all possible keys that can be used by pyautogui
print(pyautogui.KEYBOARD_KEYS)
