import requests

def consultar_cep(cep):
    cep = cep.strip().replace("-", "")
    if not cep.isdigit() or len(cep) !=8:
        print("CEP inválido! digite exatamente 8 números.")
        return
    
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado!")
        else:
            print(f"\n📍 Informações do CEP {cep}:")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")
    except requests.exceptions.RequestException as e:
        print("Erro de conexão: {e}")

cep_usuario = input("Digite o CEP (apenas números): ")
consultar_cep(cep_usuario)