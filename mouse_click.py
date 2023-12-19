import pyautogui
pyautogui.moveTo(277, 440, duration=1)

# parameters
'''
x=1611, y=507: These are the coordinates where the mouse will click.
clicks=2: This is the number of times the mouse will click.
interval=1: This is the amount of time (in seconds) between each click.
button='left': This specifies which mouse button to use for the click. In this case, its the left button.
duration=2: This is the amount of time (in seconds) it takes for the mouse to move to the specified coordinates before clicking.
'''
pyautogui.click(x=1611, y=507, clicks=2,
                interval=1, button='left', duration=2)
