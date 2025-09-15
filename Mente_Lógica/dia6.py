# 1 - Lista de convidados
# convidados = ["Renata", "Henrique", "Felipe", "Bruna"]

# for convidado in convidados:
#     print(f"{convidado}, seja bem-vinds a minha festa!")

# 2 - Estatística de Números

# entrada = input("Digite números separados por espaço: ")
# numeros = [float(num) for num in entrada.split()]

# maior_numero = max(numeros)
# menor_numero = min(numeros)
# soma_numeros = sum(numeros)
# media_numeros = soma_numeros / len(numeros)

# print("-------Estatíticas------------")
# print("Maior número", maior_numero)
# print("Menor número", menor_numero)
# print("Soma dos números", soma_numeros)
# print("Média dos números", media_numeros)

# 3 - Contagem de Caracteres em uma String:

# frase = str(input("Digite uma frase: "))
# letras = {}

# for caractere in frase:
#     if caractere.isalpha():
#         if caractere in letras:
#             letras[caractere] += 1
#         else:
#             letras[caractere] = 1

# for letra, contagem in letras.items():
#     print(f"A letra '{letra}' aparece {contagem} vez(es)")

# 4 - Ordenando uma Lista:

# entrada = input("Digite uma lista de números separados por espaço: ")
# numeros = [float(num) for num in entrada.split()]
# print(numeros)

# numeros_crescente = sorted(numeros)
# print("Numeros em ordem crescente:", numeros_crescente)

# numeros_decrescente = sorted(numeros, reverse=True)
# print("Números em ordem decrescente:", numeros_decrescente)

# meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
# numero_mes = int(input("Digite um número de 1 a 12: "))


# if numero_mes >= 1 and numero_mes <= 12:   # valida se está no intervalo correto
#     print(meses[numero_mes - 1])  # ajusta índice (1 → 0, 2 → 1, etc.)
# else:
#     print("Número inválido!")

# for i, mes in enumerate(meses):
    # if i == numero_mes:
    #     print(mes)

# Lista de tarefas

# tarefas = []

# while True:
#     print("\nMEnu de Tarefas:")
#     print("1. Adicionar Tarefa")
#     print("2. Remover Tarefa")
#     print("3. Listar Tarefa")
#     print("4. Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         tarefa = input("Digite a tarefa a ser adicionada: ")
#         tarefas.append(tarefa)
#         print("Tarefa adicionada com sucesso.")
#     elif opcao == "2":
#         tarefa = input("Digite a tarefa a ser removida: ")
#         if tarefa in tarefas:
#             tarefas.remove(tarefa)
#             print("Tarefa removida com sucesso.")
#         else:
#             print("Tarefa não encontrada.")
#     elif opcao == "3":
#         print("\nLista de Tarefas:")
#         for idx, tarefa in enumerate(tarefas, start=1):
#             print(f"{idx}. {tarefa}")
#     elif opcao == "4":
#         print("Saindo do programa.")
#         break
#     else:
#         print("Opção inválida. Tente novamente.")

# Analisador de notas:

# notas = []



# while True:

#     print("\n Menu notas")
#     print("1. Adicionar nota")
#     print("2 Sair")

#     opcao = input("Digite uma opção: ")

#     if opcao == "1":
#         nota = float(input("Digite uma nota: "))
#         notas.append(nota)
#     elif opcao == "2":
#         print("Encerrando adicionamento de notas.")
#         break
#     else:
#         print("Opção inválida.")


# if notas:
#     print(notas)
#     maior = max(notas)
#     menor = min(notas)
#     soma = sum(notas)
#     media = soma / len(notas)
#     print(f"A maior nota da turma é: {maior}") 
#     print(f"A menor nota da turma é: {menor}")
#     print(f"A média da turma é: {media}")
# else:
#     print("A lista de notas está vazia.")       
          