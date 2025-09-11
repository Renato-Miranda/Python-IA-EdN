# 1 - Calculando Troco:

# valor_pago = 20

# pao = 3.50
# leite = 4.20
# café = 2.80

# valor_total = pao + leite + café

# troco = valor_pago - valor_total

# print(f"O valor compra: {valor_total} Reais")
# print(f"O valor pago: {valor_pago} Reais")
# print(f"Troco: {troco} Reais")

# 2 - Verificando Aprovação em um Exame:

# nota_media = 8.5
# frequencia = 80 

# aprovado = (nota_media >= 7.0) and (frequencia >= 75)

# print(aprovado)

# 3 Oferta Especial:

# quantidade_itens = 8
# valor_total = 120

# tem_desconto = (quantidade_itens > 10) or (valor_total > 100)

# print(tem_desconto)

# 4 - Sistema de Acesso:

# senha_inserida = "abcd1234"
# senha_correta = "abcd1234"
# usuario_bloqueado = False

# acesso_concedido = (senha_inserida == senha_correta) and not usuario_bloqueado
# print(acesso_concedido)

# 5 - Divisão de Tarefas:

# conta = 151

# cada_um_paga = conta / 3

# eh_conta_exata = cada_um_paga % 2

# print("Cada um paga:",cada_um_paga)
# if eh_conta_exata == 0:
#     print("É conta exata! Resto:", eh_conta_exata)
# else:
#     print("Não é conta exata! Resto:", eh_conta_exata)

################### EXTRAS ###############################

# 1 - Classificação Etária

# idade = int(input("Digite a sua idade: "))
# classificacao = 16

# pode_assistir = idade > classificacao

# print("O usuário pode assistir o filme?", pode_assistir)

# 2 - Calculadora IMC

# peso = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura em metros: "))

# imc = peso / altura ** 2

# if (imc >= 18.5) and (imc <= 24.9):
#     print(f"Dentro do peso! Seu imc é {imc}")
# else:
#     print("Fora do peso ideal!")

# 3 Par ou ímpar:

# numero = int(input("Digite um número inteiro: "))

# eh_par = numero % 2 == 0

# print(eh_par)