opcao = ""
tarefas = []

while opcao != "sair":
    opcao = input("Digite uma tarefa para adicionar (ou sair para fechar): ")
    tarefas.append(opcao)
    print("Sua lista de tarefas:", tarefas)

print("Programa encerrado!")
