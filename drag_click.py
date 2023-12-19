# How to "grab" and "drag" something to another place
import pyautogui

for i in range(3):
    # Move to a coordinate
    pyautogui.moveTo(1358, 257, duration=2)

    # Click and drag to a point and release
    pyautogui.dragTo(1360, 790, button='left', duration=2)

    # Repeat 3 times