# # parâmetros opcionais com valores Padrão:

# def saudação(nome, mensagem="Seja bem-vindo."):
#     print(f"Olá {nome}! {mensagem}")

# saudação("Renato", "Como vai você?") #pode mudar o valor da mensagem !!

# #funções com retorno:
# def soma(a, b):
#     resultado = a + b
#     return resultado

# #usando a função:
# total = soma( 5, 3)
# print("O total é:", total)

# # Modificando Variáveis dentro de funções:
# contador = 0 

# def incrementar():
#     global contador
#     contador += 1 

# incrementar()
# print("Contador:",  contador)
# incrementar()
# print("Contador:",  contador)

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
    
# numero1 = float(input("Digite o primeiro número: "))
# operacao = input("Digite a operação (+ , - , * , /): ")
# numero2 = float(input("Digite o segundo número: "))

# if operacao == "+":
#     resultado = somar(numero1, numero2)
#     print(f"Resulta da soma entre {numero1} + {numero2} é igual: {resultado}")
# elif operacao == "-":
#     resultado = subtrair(numero1, numero2)
#     print(f"Resulta da subtração entre {numero1} - {numero2} é igual: {resultado}")
# elif operacao == "*":
#     resultado = multiplicar(numero1, numero2)
#     print(f"Resulta da multiplicação entre {numero1} * {numero2} é igual: {resultado}")
# elif operacao == "/":
#     resultado = dividir(numero1, numero2)
#     print(f"Resulta da divisão entre {numero1} / {numero2} é igual: {resultado}")


# 2 - Função para verificar Número primo

# def eh_primo(numero):
#     if numero <= 1:
#         return False
#     for i in range(2, numero):
#         if numero % i == 0:
#             return False
#     return True

# num = int(input("Digite um número inteiro: "))
# resultado = eh_primo(num)
# print(f"O número: {num} é primo? {resultado}")

# Conversor de temperatura:

# def celcius_para_fahrenheit(c):
#     return c * 9/5 +32
# def fahrenheit_para_celcius(f):
#     return (f - 32) * 5/9
# def celcius_para_kelvin(c):
#     return c + 273.15
# def kelvin_para_celcius(k):
#     return k - 273.15

# temperatura = float(input("Digite a temperatura: "))
# unidade = input("Digite a unidade atual (C, F, K): ").upper()
# converter_para = input("Converter para (C, F, K)").upper()

# if unidade == "C":
#     if converter_para == "F":
#         resultado = celcius_para_fahrenheit(temperatura)
#     elif converter_para == "K":
#         resultado = celcius_para_kelvin(temperatura)
# elif unidade == "F":
#     if converter_para == "C":
#         resultado = fahrenheit_para_celcius(temperatura)
#     elif converter_para == "K":
#         celcius = fahrenheit_para_celcius(temperatura)
#         resultado = celcius_para_kelvin(celcius)
# elif unidade == "K":
#     if converter_para == "C":
#         resultado = kelvin_para_celcius(temperatura)
#     elif converter_para == "F":
#         celcius = kelvin_para_celcius(temperatura)
#         resultado = celcius_para_fahrenheit(celcius)
# else:
#     resultado = "Unidade inválida."

# print(f"Temperatura convertida: {resultado} {converter_para}")

# 4 Função para Fatorial

# def fatorial(n):
#     multiplicacao = 1
#     for i in range(1, n + 1):
#         multiplicacao *= i
#     return multiplicacao

# numero = int(input("Digite um número inteiro para descobrir o fatorial: "))
# resultado = fatorial(numero)
# print(resultado)

# 4 Função recursiva para Fatorial

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)
    
# num = int(input("Digite um número inteiro positivo: "))
# if num >= 0:
#     resultado = fatorial(num)
#     print(f"O fatorial de {num} é {resultado}.")
# else:
#     print("Número inválido.")

# Gerador de senhas aleatórias:

# import random
# import string

# def senha_aleatoria(tamanho):
#     letras_maiusculas = string.ascii_uppercase
#     letras_minusculas = string.ascii_lowercase
#     numeros = string.digits
#     pontuacao = string.punctuation

#     todos_caracteres = letras_maiusculas + letras_minusculas + numeros + pontuacao

#     senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))

#     return senha

# num = int(input("Digite um número inteiro para gerar tamanho da senha: "))

# print("Senha gerada:", senha_aleatoria(num))

import math

x1 = 1
y1 = 2
x2 = 4
y2 = 6

def delta_X(x2 , x1):
    return (x2 - x1) ** 2

def delta_Y(y2, y1):
    return (y2 - y1) ** 2

def distancia(p1, p2):
    d = math.sqrt(p1 + p2)
    return d

dx2 = delta_X(x2, x1)
dy2 = delta_Y(y2, y1)

resultado = distancia(dx2, dy2)
print(f"Resultado é: {resultado}")