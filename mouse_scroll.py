import pyautogui
from time import sleep

pyautogui.moveTo(1470, 571, duration=2)

# parameters
for i in range(500):
    # scroll force
    pyautogui.scroll(-1500)
    # time between one scroll and another, give time for the internet to load
    sleep(2)
