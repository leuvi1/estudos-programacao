import sqlite3
import os
import matplotlib.pyplot as plt

print("A carregar dados da base de dados para gerar o gráfico...")

# 1. Caminho para a base de dados criada no projeto anterior

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_atual, "Ficheiros_Excel", "empresa_dados.db")

# 2. Conecta à base de dados e extrai os registos
if os.path.exists(caminho_db):
    conexao = sqlite3.connect(caminho_db)
    cursor = conexao.cursor()

    cursor.execute("SELECT nome_filial, faturamento FROM filiais")
    dados = cursor.fetchall()
    conexao.close()

    # Separa os dados em duas listas (eixo X e eixo Y)
    filiais = [linha[0] for linha in dados]
    faturamentos = [linha[1] for linha in dados]

    # 3. Criação e personalização do Gráfico de Barras
    plt.figure(figsize=(8, 5))
    plt.bar(filiais, faturamentos, color=['#2b5c8f', '#4682b4', '#5c93c4', '#78a6cc'])

    plt.title("Desempenho de Faturamento por Filial", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Filiais", fontsize=12)
    plt.ylabel("Faturamento (€)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 4. Guarda o gráfico como uma imagem PNG de alta qualidade
    caminho_grafico = os.path.join(diretorio_atual, "Ficheiros_Excel", "grafico_faturamento.png")
    plt.savefig(caminho_grafico, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"\nGráfico gerado com sucesso!")
    print(f"Imagem guardada em: {caminho_grafico}")

else:
    print(f"Aviso: Base de dados não encontrada em: {caminho_db}. Execute o projeto anterior primeiro.")
