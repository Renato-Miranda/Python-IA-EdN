def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, /, *): ")
            num2 = float(input("Digite o segundo número: "))
            

            if operacao not in ['+', '-', '/', '*']:
                print("Operação inválida! Tente novamente.")
                continue

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                    continue
                resultado = num1 / num2

            # Impressão do resultado (agora fora do if/elif)
            print(f"Resultado: {num1:.2f} {operacao} {num2:.2f} = {resultado:.2f}")
            break  # encerra o loop após operação bem-sucedida

        except ValueError:
            print("Entrada inválida. Digite apenas números.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

calculadora()