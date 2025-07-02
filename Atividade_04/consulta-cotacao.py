import requests

def consultar_cotacao(moeda):
    moeda = moeda.strip().upper()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        dados = resposta.json()

        chave = moeda + "BRL"

        if chave in dados:
            cotacao = dados[chave]
            print(f"\n Cotação {moeda}/BRL:")
            print(f"Valor atual: R$ {float(cotacao['bid']):.2f}")
            print(f"Valor máximo: R$ {float(cotacao['high']):.2f}")
            print(f"Valor mínimo: R$ {float(cotacao['low']):.2f}")
            print(f"Última atualização: {cotacao['create_date']}")
        else:
            print(" Moeda não encontrada ou inválida.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")


codigo_moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ")
consultar_cotacao(codigo_moeda)