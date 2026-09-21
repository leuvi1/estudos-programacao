def loja_capacete(tipo_capacete, quantidade_capacete):
    if tipo_capacete == 1:
        pagar = quantidade_capacete * 80
    elif tipo_capacete == 2:
        pagar = quantidade_capacete * 150
    else: 
        return "Modelo inválido" 
    if quantidade_capacete >= 4:
        return pagar * 0.90
    else:
        return pagar
capacete = int(input("Digite o tipo do capacete: "))
quantidade = int(input("Digite a quantidade de capacete vendida: "))
valor_pagar = loja_capacete(capacete, quantidade)
print("Total a pagar é: R$ ", valor_pagar)           
