import openpyxl

# 1. Abre um arquivo de excel que já existe no computador
workbook = openpyxl.load_workbook("Produtos_atualizados.xlsx")
sheet = workbook.active

print(f"Lendo a planilha: {sheet.title}\n")

# 2. Percorre todas as linhas preenchidas da planilha
for linha in range(1, 5):
    produto = sheet.cell(row=linha, column=1).value
    preco_atual = sheet.cell(row=linha, column=2).value
    preco_reajustado = sheet.cell(row=linha, column=3).value

    print(f"Produto: {produto} | Preço Atual: {preco_atual} | Reajustado: {preco_reajustado}")

print("\nLeitura concluída com sucesso pelo robô!")
