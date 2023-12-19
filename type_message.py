import pyautogui
# for special characters with accent for example import this library
import pyperclip


def write_phrase(phrase):
    pyperclip.copy(phrase)
    pyautogui.hotkey('ctrl', 'v')


# Move mouse to typing field
pyautogui.moveTo(1585, 1009, duration=2)

# Click on the typing field
pyautogui.click()

# Type my message
write_phrase('Hello, good morning!')

# Click on the send button
pyautogui.click(1880, 1003, duration=2)
