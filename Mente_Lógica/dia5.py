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
import random

programa = random.randint(1,101)
tentativas = 0

while True:
    palpite = int(input("Digite um palpite de 1 a 100: "))
    tentativas += 1
    if palpite == programa:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < programa:
        print("O número é maior!")
    else:
        print("O número é menor!")

