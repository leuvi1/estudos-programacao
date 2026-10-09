import pyautogui
import pyperclip
import time

# Configura uma pausa de 1 segundo entre cada comando do pyautogui
pyautogui.PAUSE = 1.0

# 1. Abre o menu iniciar do windows
pyautogui.press("win")
time.sleep(1)

# 2. Escreve 'chrome' e abre o navegador
pyperclip.copy("chrome")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Aguarda 3 segundos para o chrome carregar totalmente
time.sleep(3)

# 3. Move até a barra de pesquisa com as coordenadas e clica
pyautogui.moveTo(570, 413, duration=1.0)
pyautogui.click()

# 4. Copia o texto com acentos para a área de transferência
texto_pesquisa = "Automação com Python e PyAutoGUI"
pyperclip.copy(texto_pesquisa)

# 5. Cola o texto e pressiona enter
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
