def calc_imc():
    peso = float(input("Digite o peso (kg): "))
    altura_cm = float(input("Digite a altura (cm): "))
    
    altura = altura_cm / 100  # converte para metros

    imc = peso / (altura ** 2)

    print(f"IMC: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obeso")

calc_imc()