import json

pessoa = {
    "Nome": "Renato",
    "Idade": 33,
    "Cidade": "Curitiba"
}

nome_arquivo = "pessoa.json"

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
    json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)

print(f"Dados gravados em '{nome_arquivo}' com sucesso.\n")

with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
    dados_lidos = json.load(arquivo_json)

print("Dados lidos do arquivo JSON:")
print(f"Nome: {dados_lidos['Nome']}")
print(f"Idade: {dados_lidos['Idade']}")
print(f"Cidade: {dados_lidos['Cidade']}")
