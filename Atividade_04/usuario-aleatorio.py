import requests

def gerar_usuario():
    try:
        resposta = requests.get("https://randomuser.me/api/")
        resposta.raise_for_status()

        dados = resposta.json()

        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil Gerado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)
    except KeyError:
        print("Erro ao processar os dados da resposta.")


gerar_usuario()