import pyautogui

# Como tirar print da tela inteira
pyautogui.screenshot('tela.jpg')

# Como tirar um print de parte da tela
pyautogui.screenshot('calculadora.jpg', region=(1426, 159, 280, 600))
