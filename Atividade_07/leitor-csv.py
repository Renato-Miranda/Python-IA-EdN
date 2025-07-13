import csv
nome_arquivo = "pessoas.csv"

try:
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)

        print("Dados das pessoas:\n")
        for linha in leitor:
            nome = linha["Nome"]
            idade = linha["Idade"]
            cidade = linha["Cidade"]
            print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")