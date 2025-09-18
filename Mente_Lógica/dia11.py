# Agenda Telefônica:

# agenda = {}
# def adicionar_contato():
#     nome = input("Nome: ")
#     telefone = input("Telefone: ")
#     agenda[nome] = telefone
#     print("Contato adcionado com sucesso!")

# def buscar_contato():
#     nome = input("Nome contato: ")
#     if nome in agenda:
#         print(f"Telefone de {nome}: {agenda[nome]} ")
#     else:
#         print("Contato não encontrado")

# def remover_contato():
#     nome = input("Remover: ")
#     if nome in agenda:
#         del agenda[nome]
#         print(f"Contato removido com sucesso!")
#     else:
#         print("Contato não encontrado.")



# while True:
#     print("\n---Agenda Telefônica-----")
#     print("1. Adicionar contato")
#     print("2. Buscar contato")
#     print("3. Remover contato")
#     print("4. sair")
#     opcao = input("Escolha uma das opções: ")

#     if opcao == "1":
#         adicionar_contato()
#     elif opcao == "2":
#         buscar_contato()
#     elif opcao == "3":
#         remover_contato()
#     elif opcao == "4":
#         print("Saindo agenda.")
#         break
#     else:
#         print("Opção inválida. Tente novamente.")

# Verificação de Palavras Únicas:

# frase = input("Digite uma frase: ")
# palavras = frase.split()
# palavras_unicas = set(palavras)
# print("Palavras únicas:", palavras_unicas)

# contagem = {}

# for palavra in palavras:
#     if palavra in contagem:
#         contagem[palavra] += 1
#     else:
#         contagem[palavra] = 1

# print(contagem) 

# União e interseção de Conjuntos:

# numeros_a = input("Conjunto A: ").split()
# numeros_b = input("Conjunto B: ").split()

# conjunto_a = set(numeros_a)
# conjunto_b = set(numeros_b)

# uniao = conjunto_a.union(conjunto_b)
# intersecao = conjunto_a.intersection(conjunto_b)

# print(f"Conjunto A: {conjunto_a}")
# print(f"Conjunto B: {conjunto_b}")

# print(f"União dos conjuntos: {uniao}")
# print(f"Interseção dos conjuntos: {intersecao}")

texto = input("Digite seu texto: ").lower()
texto_sem_espaco = texto.replace(" ", "")
contagem = {}

for letra in texto_sem_espaco:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print("Contagem de caracteres:")
for caractere, quantidade in contagem.items():
    print(f"{caractere}: {quantidade}")