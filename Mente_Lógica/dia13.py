# Exemplos Práticos:

# 1 - Contador de Palavras em um Arquivo:
#  Imagine que você quer saber quantas vezes cada palavra aparece nas suas anotações.
# nome_arquivo = input("Digite o nome do arquivo :")

# try:
#     with open(nome_arquivo, 'r') as arquivo:
#         conteudo = arquivo.read()
# except FileNotFoundError:
#     print("Arquivo não encontrado.")
# else:
#     palavras = conteudo.lower().split()
#     contagem = {}

#     for palavra in palavras:
#         palavra = palavra.strip('.,!?":;-()')
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1

# for palavra, quantidade in contagem.items():
#     print(f"{palavra}: {quantidade}")

# Gerenciador de Contatos:
# import csv 

# def adicionar_contato():
#     nome = input("Nome: ")
#     telefone = input("Telefone: ")
#     email = input("Email: ")

#     with open('contatos.csv', 'a', newline='') as arquivo_csv:
#         escritor = csv.writer(arquivo_csv)
#         escritor.writerow([nome, telefone, email])
#     print("Contato adicionado com sucesso.")

# def listar_contatos():
#     try:
#         with open('contatos.csv', 'r') as arquivo_csv:
#             leitor = csv.reader(arquivo_csv)
#             for linha in leitor:
#                 print(f"Nome: {linha[0]}, Telefone: {linha[1]}, Email: {linha[2]}")
#     except FileNotFoundError:
#         print("Nenhum contato encontrado.")
    
# while True:
#     print("\nMenu:")
#     print("1. Adicionar Contato")
#     print("2. Listar Contatos")
#     print("3. Sair")
#     opcao = input("Escolha uma opção: ")

#     if opcao == '1':
#         adicionar_contato()
#     elif opcao == '2':
#         listar_contatos()
#     elif opcao == '3':
#         print("Encerrando Programa.")
#         break
#     else:
#         print("Opção inválida.")

# 3 Leitor de arquivos Json:
# import json

# try:
#     with open('produtos.json', 'r') as arquivo_json:
#         produtos = json.load(arquivo_json)
# except FileNotFoundError:
#     print("Arquivo não encontrado.")
# else:
#     for produto in produtos:
#         print(f"Nome: {produto['nome']}")
#         print(f"Preço: R${produto['preco']:.2f}")
#         print(f"Quantidade: {produto['quantidade']}")
#         print("-" * 20)

# 4 Copiador de Arquivos:
# origem = input("Digite o nome do arquivo de origem: ")
# destino = input("Digite o nome do arquivo de destino: ")

# try:
#     with open(origem, 'rb') as arquivo_origem:
#         conteudo = arquivo_origem.read()
#     with open(destino, 'wb') as arquivo_destino:
#          arquivo_destino.write(conteudo)
# except FileNotFoundError:
#     print("Arquivo de origem não encontrado.")
# else:
#     print(f"Arquivo de {destino} criado com sucesso.")

# Calculadora de Notas:

# import csv

# notas_alunos = []

# try:
#     with open('notas.csv', 'r') as arquivo_csv:
#         leitor = csv.DictReader(arquivo_csv)
#         for linha in leitor:
#             nome = linha['Nome']
#             nota1 = float(linha['Nota1'])
#             nota2 = float(linha['Nota2'])
#             nota3 = float(linha['Nota3'])
#             media = (nota1 + nota2 + nota3) / 3
#             notas_alunos.append({'Nome': nome, 'Media': round(media, 2)})
# except FileNotFoundError:
#     print("Arquivo de notas não encontrado.")
# except ValueError as e:
#     print("Erro:", e )
# else:
#     with open('medias.csv', 'w', newline='') as arquivo_csv:
#         campos = ['Nome', 'Media']
#         escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
#         escritor.writeheader()
#         for aluno in notas_alunos:
#             escritor.writerow(aluno)
#         print("Médias calculadas e salvas no arquivo 'medias.cv'")

# Exercícios Práticos: 

#1 - Contador de Palavras em um Arquivo.

# import csv

# nome_arquivo = input("Digite o nome do arquivo: ")

# try:
#     with open(nome_arquivo, 'r') as arquivo:
#         conteudo = arquivo.read()
# except FileNotFoundError:
#     print("Arquivo não encontrado.")
# else:
#     palavras = conteudo.lower().split()
#     contagem = {}

#     for palavra in palavras:
#         palavra = palavra.strip('.,!?";:-()')
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1

# for palavra, quantidade in contagem.items():
#     print(f"{palavra}: {quantidade}")

# 2 - Gerenciador de Contatos

# import csv

# def adicionar_contato():
#     nome = input("Nome: ")
#     telefone = input("Telefone: ")
#     email = ("Email: ")

#     with open('contatos.csv', 'a', newline='') as arquivo_csv:
#         escritor = csv.writer(arquivo_csv)
#         escritor.writerow([nome, telefone, email])
#     print("Contato adicionado com sucesso.")

# def listar_contato():
#     try:
#         with open('contatos.csv', 'r') as arquivo_csv:
#             leitor = csv.reader(arquivo_csv)
#             for linha in leitor:
#                 print(f"Nome: {linha[0]}, telefone: {linha[1]}, Email: {linha[2]}")
#     except FileNotFoundError:
#         print("Nenhum contado encontrado.")


# while True:
#     print("Menu:")
#     print("1. Adicionar contato")
#     print("2. Listar contato")
#     print("3. Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == '1':
#         adicionar_contato()
#     elif opcao == '2':
#         listar_contato()
#     elif opcao == '3':
#         break
#     else: 
#         print("Opção inválida.")


# 3 Leitor de Arquivos JSON

# import json

# try:
#     with open('produtos.json', 'r') as arquivo_json:
#         produtos = json.load(arquivo_json)
# except FileNotFoundError:
#     print("Arquivo não encontrado.")
# else:
#     for produto in produtos:
#         print(f"Nome: {produto['nome']}")
#         print(f"Preço: R${produto['preco']:.2f}")
#         print(f"Quantidade: {produto['quantidade']}")

# 4 Copiador de Arquivos

origem = input("Digite o nome do arquivo de origem: ")
destino = input("Digite o nome do arquivo de destino: ")

try:
    with open(origem, 'rb') as arquivo_origem:
        conteudo = arquivo_origem.read()
    with open(destino, 'wb') as arquivo_destino:
        arquivo_destino.write(conteudo)
except FileNotFoundError:
    print("Arquivo de origem não encontrado.")
else:
    print(f"Arquivo {destino} criado com sucesso.")