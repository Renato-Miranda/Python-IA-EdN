def calcular_gorjeta():
    valor_total = float(input("Digite o valor total da compra: "))
    porcentagem_gorjeta = float(input("Qual a porcentagem da gorjeta: "))

    valor_gorjeta = valor_total * (porcentagem_gorjeta / 100)
    valor_final = valor_total + valor_gorjeta

    print(f"Gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"Valor total com gorjeta: R$ {valor_final:.2f}")
    
calcular_gorjeta()