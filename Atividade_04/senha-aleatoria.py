import random
import string

def criar_senha():
    try:
        tamanho_senha = int(input("Digite o tamanho da senha a ser gerada: "))
    except ValueError:
        print("Por favor digite um tamanho válido.")
        return
    
    if tamanho_senha < 4:
        print("Senha deve ter tamanho mínimo de 4 caracteres")
        return
    caracteres_especiais = string.punctuation

    senha = ''.join(random.choice(caracteres_especiais) for _ in range(tamanho_senha))

    print(f"Sua senha especial é: {senha}")

criar_senha()