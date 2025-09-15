# 1 - Imprimindo números de 1 a 10
# for numero in range(1,11):
#     print("Nummero:", numero)

# 2 - Calculando a Soma dos Números de 1 a N

# n = int(input("Digite um número inteiro: "))
# soma = 0

# for numero in range(1, n+1):
#     soma += numero

# print(soma)

# 3 Tabuada de um Número 

# numero = int(input("Digite um número inteiro: "))

# for i in range(1,11):
#     resultado = numero * i
#     print(resultado)

# 4 Contador de Impar e Par
# par = 0
# impar = 0
# for i in range(1,25):
#     if i % 2 == 0:
#         par += 1
#     elif i % 2 !=0:
#         impar += 1
#     else:
#         print("nada aqui!")

# print("Par:",par)
# print("Impar:",impar)

# 5 Adivinhe o Número:
# import random

# programa = random.randint(1,101)
# tentativas = 0

# while True:
#     palpite = int(input("Digite um palpite de 1 a 100: "))
#     tentativas += 1
#     if palpite == programa:
#         print(f"Parabéns! Você acertou em {tentativas} tentativas.")
#         break
#     elif palpite < programa:
#         print("O número é maior!")
#     else:
#         print("O número é menor!")

#################################### Extras

# Calculando Fatorial de um número

# N = int(input("Digite um número inteiro para descobrir o seu Fatorial: "))

# multiplicacao = 1

# for i in range(1, N + 1):
#     multiplicacao *= i

# print(multiplicacao)

# sequencia Fibonacci

N = int(input("Digite um número inteiro: "))

termo1 = 0
termo2 = 1
contador = 0 

if N <=0 :
    print("Digite um número positivo")
elif N == 1:
    print("Serie Fibonacci até", N, "Termo:")
    print(termo1)
else:
    print("Serie Fibonacci:")
    while contador < N:
        print(termo1)
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
        contador +=1

# Jogo da forca:

palavra_secreta = "machado"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 7

while tentativas > 0 and "_" in letras_descobertas:
    print("Palavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
                print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")

if "_" not in letras_descobertas:
    print("Parabéns! você adivinhou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)