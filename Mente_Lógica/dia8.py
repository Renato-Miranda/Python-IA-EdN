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

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return  a / b
    else:
        return "Erro: Divisão por zero!"
    
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+ , - , * , /): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = somar(numero1, numero2)
    print(f"Resulta da soma entre {numero1} + {numero2} é igual: {resultado}")
elif operacao == "-":
    resultado = subtrair(numero1, numero2)
    print(f"Resulta da subtração entre {numero1} - {numero2} é igual: {resultado}")
elif operacao == "*":
    resultado = multiplicar(numero1, numero2)
    print(f"Resulta da multiplicação entre {numero1} * {numero2} é igual: {resultado}")
elif operacao == "/":
    resultado = dividir(numero1, numero2)
    print(f"Resulta da divisão entre {numero1} / {numero2} é igual: {resultado}")






