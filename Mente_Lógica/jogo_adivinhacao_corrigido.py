import random

pontuacoes = []

print("Bem-vindo ao jogo de Adivinhação!")
dificuldade = input("\nSelecione uma dificuldade: Fácil = 'f', Média = 'm', Difícil = 'd': ").lower()

modo = ''

while True:
    numero_secreto = random.randint(1, 100)
    if dificuldade == 'f':
        modo = "Fácil"
        tentativas_restantes = 10
    elif dificuldade == 'm':
        modo = "Média"
        tentativas_restantes = 7
    elif dificuldade == 'd':
        modo = "Difícil"
        tentativas_restantes = 4
    tentativas = 0

    print("\nEu pensei em um número entre 1 a 100.")
    print(f"Você escolheu o modo: {modo}.")
    print(f"Você tem {tentativas_restantes} tentativas para adivinhar.")

    #loop de tentativas
    while tentativas_restantes > 0:
        palpite = input("\nDigite seu palpite: ")

        #verificando se o input é um número válido
        if not palpite.isdigit():
            print("Por favor, digite um número inteiro válido. Entre 1 e 100")
            continue

        palpite = int(palpite)

        if palpite < 1 or palpite > 100:
         print("O número deve estar entre 1 e 100")
         continue

        tentativas += 1
        tentativas_restantes -= 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            pontuacao = tentativas_restantes * 10
            pontuacoes.append(pontuacao)
            print(f"Sua pontuação nesta partida: {pontuacao} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número é maior que esse.")
        else:
            print("O número é menor que esse.")

        print(f"Tentativas restantes: {tentativas_restantes}")

    else:
        print(f"\nQue pena! Você não conseguiu adivinhar. O número secreto era {numero_secreto}")
        pontuacoes.append(0)

        #Exibindo o placar
        print("\nPlacar:")
        for i, pontos in enumerate(pontuacoes, start=1):
            print(f"Partida {i}: {pontos} pontos")

        #Perguntar se o jogador quer jogar novamente
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            print("Obrigado por jogar! Até a próxima.")
            break