import string

def eh_palindromo():
    texto_original = str(input("Digite uma palavra para verificar se é palindrimo: ")).lower()

    if any(char.isdigit() for char in texto_original):
        print("Por favor, digite uma palavra ou frase sem números.")
        return

    texto_tratado = ''. join(char for char in texto_original if char.isalnum())
    texto_invertido = texto_tratado[::-1]

    if not texto_tratado:
        print("Entrada inválida. Digite uma palavra ou frase com letras.")
        return

    if texto_tratado == texto_invertido:
        print(f"Sim! a palavra: {texto_original} é um palindromo!")
        print(texto_invertido)
    else:
        print(f"Não! a palavra: {texto_original} não é um palindromo!")
        print(texto_invertido)


eh_palindromo()

