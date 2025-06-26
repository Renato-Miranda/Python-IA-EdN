def converter_moeda():
    valor_reais = int(input("Qual o valor a ser convertido? "))
    taxa_dolar = 5.20
    taxa_euro = 6.15

    dolar = valor_reais * taxa_dolar
    euro = valor_reais * taxa_euro

    print(
        f"R${valor_reais} convertido em dólar fica: ${dolar:.2f}",
        f"R${valor_reais} convertido em Euro fica: ${euro:.2f}",
        sep="\n"
        )

def main():
 converter_moeda()    

main()