# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

def verificar_ano():
    ano = int(input("Digite o ano para verificar se é bissexto: "))
    bissexto = ano % 4 == 0

    if bissexto is True:
        print(f"O ano de {ano} é Bissexto!" )
    else:
        print(f"O ano de {ano} não é Bissexto!")


verificar_ano()