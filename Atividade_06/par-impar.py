def par_ou_impar():

    qtd_pares = 0
    qtd_impares = 0 

    while True:
        entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"{numero} é par.")
                qtd_pares += 1
            else:
                print(f"{numero} é ímpar.")
                qtd_impares += 1

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros ou 'fim' para sair.")

    print("\nResumo:")
    print(f"Quantidade de números pares: {qtd_pares}")
    print(f"Quantidade de números ímpares: {qtd_impares}")

par_ou_impar()