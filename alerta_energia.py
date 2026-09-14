try:
    with open("consumo.txt", "r") as arquivo:
        for linha in arquivo:
            linha_linha = linha.strip()
            pedacos = linha_linha.split(":")
            consumo = int(pedacos[1])
            if consumo > 600:
                print(f" ALERTA: {pedacos[0]} está com consumo alto ({consumo}w)!")
except FileNotFoundError:
    print("Erro: O arquivo consumo.txt não foi encontrato!")  
