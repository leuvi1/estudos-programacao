opcao = 1

while opcao != 0:
    print("\n -- CADASTRO ACADEMIA -- ")
    print("1 - Registrar Nome do Aluno")
    print("2 - Registrar Peso (Kg)")
    print("0 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nome_aluno = input("Digite o nome do aluno: ")
        print(f"Aluno {nome_aluno} registrado com sucesso")
    elif opcao == 2:
        peso_aluno = float(input("Digite o peso do aluno: "))
        print(f"Peso {peso_aluno} Kg registrado com sucesso")
    elif opcao == 0:
        print("Finalizando cadastro...")
    else:
        print("Opção inválida!")
