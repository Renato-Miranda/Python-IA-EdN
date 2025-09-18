# 1 Calculadora de funções

# def somar(a, b):
#     return a + b

# def subtrair(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b != 0:
#         return  a / b
#     else:
#         return "Erro: Divisão por zero!"
# try:    
#     numero1 = float(input("Digite o primeiro número: "))
#     operacao = input("Digite a operação (+ , - , * , /): ")
#     numero2 = float(input("Digite o segundo número: "))

#     if operacao == "+":
#         resultado = somar(numero1, numero2)
#         print(f"Resulta da soma entre {numero1} + {numero2} é igual: {resultado}")
#     elif operacao == "-":
#         resultado = subtrair(numero1, numero2)
#         print(f"Resulta da subtração entre {numero1} - {numero2} é igual: {resultado}")
#     elif operacao == "*":
#         resultado = multiplicar(numero1, numero2)
#         print(f"Resulta da multiplicação entre {numero1} * {numero2} é igual: {resultado}")
#     elif operacao == "/":
#         resultado = dividir(numero1, numero2)
#         print(f"Resulta da divisão entre {numero1} / {numero2} é igual: {resultado}")
# except (ValueError , ZeroDivisionError) as e:
#     print(f"Erro: {e}")

#Acesso a arquivos com Tratamento de Exceções:

# import os

# try:
#     arquivo = open('dados.txt', 'r')
#     conteudo = arquivo.read()
# except FileNotFoundError as fnf:
#         print(f"Erro: {fnf}")
# except Exception as e:
#      print(f"Ocorreu um erro inesperado: {e}")
# else: 
#     print("Arquivo lido com sucesso!")
# finally:
#      if 'arquivo' in locals():
#         arquivo.close()
#         print("Arquivo fechado.")