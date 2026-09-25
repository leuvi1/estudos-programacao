opcao = 1

while opcao != 0:
    print("\n -- CALCULADORA DE MULTIPLICAÇÃO --")
    print("1 - Calcular o dobro")
    print("2 - Calcular o triplo")
    print("3 - Calcular o quadruplo")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        numero = int(input("Digite um número: "))
        dobro = numero * 2
        print("O dobro é: ", dobro)

    elif opcao == 2:
        numero = int(input("Digite um número: "))
        triplo = numero * 3
        print("O triplo é: ", triplo)

    elif opcao == 3:
        numero = int(input("Digite um número: "))
        quadruplo = numero * 4
        print("O quadruplo é: ", quadruplo)

    elif opcao == 0:
        print("Saindo da calculadora...")

    else:
        print("Opcao inválida!")
