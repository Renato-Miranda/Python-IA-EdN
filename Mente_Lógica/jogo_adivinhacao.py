import random

print("Bem-vindo ao jogo de adivinhação.")
numero_secreto = random.randint(1, 100)
tentativas = 7
pontuacoes = []


while tentativas > 0:
    palpite = int(input("Digite um número inteiro entre 1 e 100: "))
    if palpite == numero_secreto:
        print(f"Parabéns você acertou! restando {tentativas} tentativas.")
        pontuacao = tentativas * 2
        print(f"Sua pontuação foi de: {pontuacao} ")
        decisao = input("Para jogar novamente digite 'n'. Sair 's': ")
        if decisao == "n":
            print("Vamos continuar o jogo!")
            pontuacoes.append(pontuacao)
            numero_secreto = random.randint(1, 100)
            tentativas = 7
            continue
        elif decisao == "s":
            pontuacoes.append(pontuacao)
            print("Saindo do jogo.")
            print(f"suas pontuações foram: {pontuacoes}")
            break
        else:
            print("Opção inválida!")
    elif palpite > numero_secreto:
        print("O número é Menor!")
        tentativas -= 1
        print(f"Tentativas: {tentativas}")
    elif palpite < numero_secreto:
        print("O número é Maior!")
        tentativas -=1
        print(f"Tentativas: {tentativas}")

    if tentativas == 0:
        print("Você não tem mais tentativas! ")
        print(f"O número secreto era {numero_secreto}")
        continuar = input("Você deseja jogar novamente? Sim digite: 'sim'. Sair digite: 'sair' ")
        if continuar == 'sim':
            print('Continuando o jogo!')
            print(f"Suas pontuações até o momento são: {pontuacoes}")
            numero_secreto = random.randint(1, 100)  # gera novo número
            tentativas = 7  # reinicia tentativas
            continue
        elif continuar == 'sair':
            print("Terminando o jogo!")
            print(f"Suas pontuações foram: {pontuacoes}")
            break

        