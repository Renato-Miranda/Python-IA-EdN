# import conversoes

# fahrenheit = conversoes.celcius_para_fahrenheit(25)

# print(fahrenheit)

# import random 

# def jogo_adivinhação():

#     numero_secreto = random.randint(1, 100)
#     tentativas = 7
    
#     while tentativas > 0:
#         palpite = int(input("Digite seu palpite entre 1 a 100: "))
#         if palpite == numero_secreto:
#             print(f"Parabéns! Você acertou o número secreto.")
#             break
#         elif palpite > numero_secreto:
#             print("O número secreto é menor.")
#             tentativas -= 1
#             print(f"Tentativas restantes: {tentativas}")
#         elif palpite < numero_secreto:
#             print("O número secreto é maior.")
#             tentativas -= 1
#             print(f"Tentativas restantes: {tentativas}")
#         else: 
#             print('Opção inválida, perde uma tentativa')
#             tentativas -= 1

# jogo_adivinhação()

import os

def manipular_arquivos():
    #Criando uma pasta
    os.mkdir('nova_pasta')
    print("Pasta 'nova_pasta' criada.")

    #mudando para novo diretório
    os.chdir('nova_pasta')

    #criando um arquivo
    with open('arquivo.txt', 'W') as arquivo:
        arquivo.write("Este é um arquivo dentro da nova pasta.")
        print("Arquivo 'arquivo.txt' criado dentro de 'nova_pasta'.")

    # Listando arquivos
    arquivos = os.listdir('.')
    print("Arquivos no diretório atual:", arquivos)

manipular_arquivos()