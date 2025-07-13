import csv

# Lista de pessoas com seus dados
pessoas = [
    {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Carlos", "Idade": 35, "Cidade": "Rio de Janeiro"},
    {"Nome": "Beatriz", "Idade": 22, "Cidade": "Curitiba"},
    {"Nome": "Renato", "Idade": 33, "Cidade": "Curitiba"},
]

# Nome do arquivo CSV a ser criado
nome_arquivo = "pessoas.csv"

# Escrevendo no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Definindo os nomes das colunas
    colunas = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

    # Escreve o cabeçalho
    escritor.writeheader()

    # Escreve os dados das pessoas
    for pessoa in pessoas:
        escritor.writerow(pessoa)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
