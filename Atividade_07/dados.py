import csv

pessoas = [
    {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Carlos", "Idade": 35, "Cidade": "Rio de Janeiro"},
    {"Nome": "Beatriz", "Idade": 22, "Cidade": "Curitiba"},
    {"Nome": "Renato", "Idade": 33, "Cidade": "Curitiba"},
]

nome_arquivo = "pessoas.csv"

with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    colunas = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

    escritor.writeheader()

    for pessoa in pessoas:
        escritor.writerow(pessoa)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
