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

#Conversão de dados com Tratamento de Exceções:

# def obter_idade():
#     while True:
#         try:
#             idade = int(input("Digite sua idade: "))
#             if idade < 0:
#                 raise ValueError ("A idade não pode ser negativa.")
#             return idade
#         except ValueError as ve:
#             print(f"Erro: {ve}")

# idade_usuario = obter_idade()
# print(f"Sua idade é: {idade_usuario}")

# 1. Divisão segura:

# def divisao_segura():
#     try:
#         numero1 = float(input("Digite o primeiro número: "))
#         numero2 = float(input("Dividir por: "))
#         resultado = numero1 / numero2
#     except ValueError as ve:
#         print(f"Erro de valor: {ve}")
#     except ZeroDivisionError:
#         print("Erro divisão por zero, Tente outro número.")
#     else:
#         print(f"A divisão de {numero1} por {numero2} é: {resultado}")


# divisao_segura()

# Abertura de Arquivo com Verificação:

# def ler_arquivo_usuario():
#     nome_arquivo = input("Digite o nome do arquivo: ")
#     try:
#         with open(nome_arquivo, 'r') as arquivo:
#             conteudo = arquivo.read()
#             print(conteudo)
#     except FileNotFoundError:
#         print("Erro: O arquivo não existe.")
#     except PermissionError:
#         print("Erro: Sem permissão para ler o arquivo.")
#     except Exception as e:
#         print(f"Ocorreu um erro: {e}")

# ler_arquivo_usuario()

# 3 Conversão de Temperaturas com Validação.

def celcius_para_fahrenheit():
    try:
        celcius = float(input("Digite a temperatura em celcius: "))
        fahrenheit = celcius * 9/5 + 32
    except ValueError:
        print("Erro: Por favor, insira um valor numérico.")
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

celcius_para_fahrenheit()