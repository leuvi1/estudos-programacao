def calcular_tarifas(horas):
    if horas <= 1:
        return 0.00
    elif horas <= 4:
        return 10.00
    else:
        return 25.00
      
horas_cliente = float(input("Digite quantas horas o carro ficou no estacionamento: "))  
valor_pago = calcular_tarifas(horas_cliente)  
print("Valor a pagar: ", valor_pago)
