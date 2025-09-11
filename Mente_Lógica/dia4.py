# 1 - Verificando Se um Número é Positivo, Negativo ou Zero

# numero = float(input("Digite um número: "))

# if numero > 0:
#     print(f"O número: {numero} é Positivo")
# elif numero< 0:
#     print(f" O número: {numero} é Negativo")
# else:
#     print(f"O número: {numero} é Zero")

# 2 - Calculadora Simples

# numero1 = float(input("Digite o primeiro número: "))
# operacao = str(input("Digite uma operação '*', '/', '+', '-': "))
# numero2 = float(input("Digite o segundo número: "))


# if operacao == '*':
#     resultado = numero1 * numero2
# elif operacao == '/':
#     if numero2 != 0:
#        resultado = numero1 / numero2
#     else:
#         resultado = "Erro"
#         print(f"{resultado}: Divisão por zero!")    
# elif operacao == '+':
#     resultado = numero1 + numero2
# elif operacao == '-':
#     resultado = numero1 - numero2
# else:
#     print("Operação não permitida!")

# print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")

# 3.Classificação de Idade:

# idade = int(input("Digite uma idade: "))

# if idade >= 0 and idade <= 12:
#     print("Criança")
# elif idade > 12 and idade <= 17:
#     print("Adolescente")
# elif idade > 17 and idade <= 59:
#     print("Adulto")
# else:
#     print("Idoso")

#4 - Verificando Ano Bissexto

# ano = int(input("digite um ano: "))

# if ano % 4 == 0 or ano % 100 == 0:
#     print("Ano Bissesto!!!!")
# else: 
#     print("Não é ano Bissexto!")

#5 - Simulador de Caixa Eletrônico

# valor_saque = int(input("Digite o valor do saque: R$"))

# if valor_saque <= 0:
#      print("Valor inválido.")
# else:
#     cedulas_100 = valor_saque // 100
#     valor_saque %= 100
#     cedulas_50 = valor_saque // 50
#     valor_saque %= 50
#     cedulas_20 = valor_saque // 20
#     valor_saque %= 20
#     cedulas_10 = valor_saque // 10
#     valor_saque %= 10
#     cedulas_5 = valor_saque // 5
#     valor_saque %= 5
#     cedulas_2 = valor_saque // 2
#     valor_saque %= 2

#     if valor_saque != 0:
#         print("Não é possível sacar o valor especificado com as cédulas disponíveis.")
#     else:
#         print("Cédulas entregues:")

# if cedulas_100 > 0:
#  print(f"{cedulas_100} x R$100")
# if cedulas_50 > 0:
#  print(f"{cedulas_50} x R$50")
# if cedulas_20 > 0:
#  print(f"{cedulas_20} x R$20")
# if cedulas_10 > 0:
#  print(f"{cedulas_10} x R$10")
# if cedulas_5 > 0:
#  print(f"{cedulas_5} x R$5")
# if cedulas_2 > 0:
#  print(f"{cedulas_2} x R$2")

# 5 - Aprovando Empréstimo Bancário

# valor_emprestimo = float(input("Digite valor do empréstimo: "))
# renda_mensal = float(input("Digite sua renda mensal: "))
# numero_pacelas = float(input("Digite o número de parcelas: "))

# valor_parcela = valor_emprestimo / numero_pacelas
# porcentegem_renda = renda_mensal * 0.3 

# if valor_parcela <= porcentegem_renda:
#     print(f"Empréstimo aprovado! Valor da parcela: {valor_parcela}")
# else:
#     print(f"Empréstimo nagado! Valor da parcela: {valor_parcela}")

# Pedra, papel ou tesoura:

# import random

# opcoes = ["pedra", "papel", "tesoura"]

# usuario = str(input("Escolha pedra, papel ou tesoura: ")).lower()
# computador = random.choice(opcoes)

# print(f"Você escolheu: {usuario}")
# print(f"O computador escolheu: {computador}")

# if usuario == computador:
#     print("Empate!")
# elif (usuario == "pedra" and computador == "tesoura") or \
#      (usuario == "papel" and computador == "pedra") or \
#      (usuario == "tesoura" and computador == "papel"):
#     print("Você venceu!")
# elif usuario in opcoes:
#     print("Você perdeu!")
# else:
#     print("escolha inválida!")

# Calculadora de tarifas de Táxi:

distancia = float(input("Digite a distância rodada em KM: "))
valor_rodado = distancia * 0.25
tarifa_basica = 4

valor_total = tarifa_basica + valor_rodado
print(f"O valor total da corrida é: R${valor_total}")
