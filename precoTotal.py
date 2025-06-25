def main():

    def preco_total():
        produto = "Cadeira Infantil"
        preco_unitario = 12.40
        quantidade = int(input("Quantas unidades: "))
        preco_total = preco_unitario * quantidade
        print(f"Quantidade: {quantidade}")
        print(f"Produto: {produto}")
        print(f"O valor total é de: {preco_total} Reais.")

    preco_total()    

main()