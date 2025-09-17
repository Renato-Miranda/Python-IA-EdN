# frase = input("Digite uma frase para contar as vogais: ").lower()
# vogais = 'aeiou'
# contador = 0


# for letra in frase:
#     if letra in vogais:
#         contador += 1


# if contador > 0:   
#     print(f"Essa frase contêm {contador} vogais.")
# else:
#     print("Não sei como, mas essa frase não tem vogais")

# # Invertendo Palavras:

# frase = input("Digite uma frase a ser invertida: ")
# frase_invertida = ''.join(reversed(frase))
# # ou
# frase_invertida2 = frase[::-1]

# print(f"Frase invertida usando Reversed: {frase_invertida}")
# print(f"Frase invertida usando [::-1]: {frase_invertida2}")

# frase = str(input("Digite usa palavra ou frase: ")).lower()
# frase_sem_espaco = frase.replace(" ", "")
# print(frase_sem_espaco)
# frase_invertida = ''.join(reversed(frase_sem_espaco))
# print(frase_invertida)

# if frase_invertida == frase_sem_espaco:
#     print("É um palíndromo.")
# else:
#     print("Não é um palíndromo.")

# senha forte:

import string

senha = input("Digite uma senha forte: ")

tem_maisculas = any(c.isupper() for c in senha)
tem_minusculas = any(c.islower() for c in senha)
tem_numeros = any(c.isdigit() for c in senha)
simbolos = any(not c.isalnum() for c in senha)
tamanho_adequado = len(senha) >= 8

if tem_maisculas and tem_minusculas and tem_numeros and simbolos and tamanho_adequado:
    print("Sua senha é forte!")
else:
    print("Sua senha é fraca. Tente novamente")

