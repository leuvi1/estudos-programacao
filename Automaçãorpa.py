import pyautogui
import time

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho

pyautogui.PAUSE = 1

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Abrir o navgegador
pyautogui.press("win")
pyautogui.write("google ")
pyautogui.press("enter")
pyautogui.click(x=490, y=413)
pyautogui.write("Gran Faculdade")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=231, y=398)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=1084, y=153)
time.sleep(5)
pyautogui.click(x=190, y=611)
