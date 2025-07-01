# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

def verificar_ano():
    ano = int(input("Digite o ano para verificar se é bissexto: "))

    if (ano % 4 ==0 and ano % 100 !=0) or (ano % 400 == 0):
        print(f"O ano de {ano} é Bissexto!" )
    else:
        print(f"O ano de {ano} não é Bissexto!")


verificar_ano()