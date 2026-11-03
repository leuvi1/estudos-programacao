import time
import pyautogui
import pyperclip

# Configuração de segurança
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

print("Iniciando a automação de interface...")
time.sleep(2)

# 1. Abre o menu Iniciar e o Bloco de Notas
pyautogui.press('win')
time.sleep(1)
pyautogui.write('notepad', interval=0.1)
pyautogui.press('enter')
time.sleep(1.5)

# 2. Texto com acentos e formatação correta
texto_relatorio = """
========================================
RELATÓRIO AUTOMÁTICO DE DESKTOP
Gerado por Robô Python - PyAutoGUI
========================================
Status: Operacional e Concluído com Sucesso.
Data: Rotina de Execução Automática."""

# 3. Copia o texto para a área de transferência do Windows
pyperclip.copy(texto_relatorio)

# 4. Cola o texto instantaneamente usando Ctrl + V (suporta todos os acentos)
pyautogui.hotkey('ctrl', 'v')

print("Texto colado com sucesso, incluindo todos os acentos!")
