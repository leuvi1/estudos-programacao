def calcular_banho(peso):
    if peso <= 5:
        return 40.00
    elif peso <= 15:
        return 60.00
    else:
        return 90.00
banho_pet = float(input("Digite o peso do animal: "))
valor_final = calcular_banho(banho_pet) 
print("O valor a ser pago pelo serviço é: R$ ", valor_final) 
