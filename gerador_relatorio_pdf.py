import os
import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

print("A preparar a geração do Relatório PDF executivo...")

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_atual, "Ficheiros_Excel", "empresa_dados.db")
caminho_gafico = os.path.join(diretorio_atual, "Ficheiros_Excel", "grafico_faturamento.png")
caminho_pdf = os.path.join(diretorio_atual, "Ficheiros_Excel", "Relatorio_Executivo_Empresa.pdf")

# 1. Verifica se os recursos anteriores existem
if not os.path.exists(caminho_db) or not os.path.exists(caminho_gafico):
    print("Aviso: Base de dados ou gráficos não encontrados. Certifique-se de executar os módulos anteriores primeiro.")
else:
    # Obtém os dados da base de dados para a tabela do PDF
    conexao = sqlite3.connect(caminho_db)   
    cursor = conexao.cursor()
    cursor.execute("SELECT nome_filial, faturamento, data_registo FROM filiais")
    dados_tabela = [["Filial", "Faturamento, (€)", "Data de Registo"]] # Cabeçalho
    for linha in cursor.fetchall():
        dados_tabela.append([linha[0], f"€{linha[1]:,.2f}", linha[2]]) 
    conexao.close()

    # 2. Configuração do documento PDF (A4)
    doc = SimpleDocTemplate(caminho_pdf, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    elementos = []

    # Estilos de texto
    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle(
        'TituloEmpresa',
        parent=estilos['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#1f4e78'),
        spaceAfter=15,
        alignment=1 # Centralizado
    )
    estilo_sub = ParagraphStyle(
        'SubtituloEmpresa',
        parent=estilos['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#595959'),
        spaceAfter=20,
        alignment=1
    )

    # Adiciona elementos ao PDF
    elementos.append(Paragraph("RELATÓRIO DE DESEMPENHO OPERACIONAL", estilo_titulo))
    elementos.append(Paragraph("Documento gerado automaticamente pelo robô Python | Sistema Integrado", estilo_sub))
    elementos.append(Spacer(1, 10))

    # 3. Adiciona a Tabela formatada
    tabela = Table(dados_tabela, colWidths=[150, 150, 150])
    # 3. Adiciona a Tabela formatada
tabela = Table(dados_tabela, colWidths=[150, 150, 150])
tabela.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4e78')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f2f2f2')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d9d9d9')),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('TOPPADDING', (0, 1), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
]))
elementos.append(tabela)
elementos.append(Spacer(1, 20))

    # 4. Adiciona o Gráfico gerado anteriormente
if os.path.exists(caminho_gafico):
        # Redimensiona a imagem proporcionalmente para caber no PDF
        img = Image(caminho_gafico, width=420, height=260)
        elementos.append(img)

    # Constrói o PDF final
doc.build(elementos)
print(f"\nRelatório em PDF gerado com sucesso!")
print(f"Ficheiro guardado em: {caminho_pdf}")
