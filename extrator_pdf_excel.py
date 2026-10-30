import os
from pypdf import PdfReader
import openpyxl

print("Iniciando o processo de extração de dados de PDFs...")

# 1. Diretórios de trabalho
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_pdfs = os.path.join(diretorio_atual, "Ficheiros.PDF")
os.makedirs(pasta_pdfs, exist_ok=True)

# 2. Criação de um ficheiro Excel para receber os dados extraídos
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Dados Extraídos"

# Cabeçalhos da tabela
ws.append(["Nome do Ficheiro", "Número da Página", "Texto Extraído"])

# 3. Varre a pasta de PDFs
contador_lidos = 0
if os.path.exists(pasta_pdfs):
    ficheiros_pdfs = [f for f in os.listdir(pasta_pdfs) if f.endswith(".pdf")]

    if not ficheiros_pdfs:
        print(f"Aviso: Nenhum ficheiro PDF encontrado na pasta: {pasta_pdfs}")
        print("Dica: Coloque alguns ficheiros .pdf nessa pasta pra testar a extração real.")
    else:
        for ficheiro in ficheiros_pdfs:
            caminho_pdf = os.path.join(pasta_pdfs, ficheiro)    
            print(f"Lendo ficheiro: {ficheiro}")

            try:
                leitor = PdfReader(caminho_pdf)
                for i, pagina in enumerate(leitor.pages):
                    texto = pagina.extract_text()
                    # Adiciona uma linha na planilha com os dados encontrados
                    ws.append([ficheiro, i + 1, texto.strip()[:100] + "..."]) # Limita o texto para visualização
                contador_lidos += 1
            except Exception as e:
                print(f"Erro ao ler o ficheiro {ficheiro}: {e}")   

# Salva o resultado consolidado
caminho_excel_saida = os.path.join(diretorio_atual, "Ficheiros_Excel", "Relatorio_Extraido_PDFs.xlsx")  
os.makedirs(os.path.dirname(caminho_excel_saida), exist_ok=True)  
wb.save(caminho_excel_saida) 

print(f"\nProcesso concluído! {contador_lidos} ficheiros PDF processados.")
print(f"Dados consolidados guardados em: {caminho_excel_saida}")
