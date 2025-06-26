def calculadora_desconto():
    produto = "Camiseta"
    preco_original = 50
    desconto = int(input("Qual a porcentagem do desconto: "))
    valor_do_desconto =  preco_original * (desconto/100)
    preco_com_desconto = preco_original - valor_do_desconto

    print(
        f"Valor do desconto: R${valor_do_desconto:.2f}",
        f"Valor com desconto: R${preco_com_desconto}",
        sep="\n"
    )

def main():
    calculadora_desconto()
main()