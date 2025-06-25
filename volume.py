def main():

    def calcular_volume():
        comprimento = int(input("Comprimento: "))
        largura = int(input("Largura: "))
        altura = int(input("altura: "))
        volume = comprimento * largura * altura
        print("O volume da caixa é:", volume, "cm³.")

    calcular_volume()

main()