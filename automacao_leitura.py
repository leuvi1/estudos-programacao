import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1.0

# 1. Ler os termos do arquivo externo
# O modo "r" (read) abre o arquivo apenas para leitura
with open("pesquisas.txt", "r", encoding="utf-8") as arquivo_origem:
    # .readlines() lê todas as linhas e transforma uma linha de textos
    # .strip() remove espaços extras e quebras de linha (\n)
    listas_pesquisas = [linha.strip() for linha in arquivo_origem if linha.strip()]

# 2. Abre o Chrome de forma mais segura
pyautogui.press("win")
time.sleep(1.5)  # Dá mais tempo para a pesquisa do Windows carregar
pyperclip.copy("google chrome")  # Força o termo exato
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)
pyautogui.press("enter")
time.sleep(3.0)  # Garante que o Chrome abre totalmente

# 3. Prepara o arquivo de resultado (modo "w" para manter limpo)
with open("resultados_dinamicos.txt", "w", encoding="utf-8") as arquivo_destino:
    arquivo_destino.write("=== RELATÓRIO DINÂMICO DE PESQUISAS ===\n\n")

    for termo in listas_pesquisas:
        # Acessa a barra do chrome
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.5)
        pyperclip.copy(f"https://www.google.com/search?q={termo}")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(2.5)

        # Copia o conteúdo da página
        pyautogui.click(500, 500)
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)

        texto_bruto = pyperclip.paste()

        # Filtro de limpeza
        linhas = [linha.strip() for linha in texto_bruto.split("\n") if linha.strip()]
        linhas_filtradas = []
        for linha in linhas:
            if not any(sujeira in linha.lower() for sujeira in ["acessibilidade", "mudar idioma", "ajuda", "chatgpt", "deepseek", "aitopia"]):
                linhas_filtradas.append(linha)

        # Seleciona o trecho útil
        resumo_limpo = "\n".join(linhas_filtradas[10:15])

        # Grava no relatório
        arquivo_destino.write(f"TERMO PESQUISADO: {termo}\n")
        arquivo_destino.write(f"RESUMO: \n{resumo_limpo}\n")
        arquivo_destino.write("=" * 50 + "\n\n")

print("Automação dinâmica concluída!")
