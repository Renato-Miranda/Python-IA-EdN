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