def calcular_media():
    nota1 = int(input("Digite a nota 01: "))
    nota2 = int(input("Digite a nota 02: "))
    nota3 = int(input("Digite a nota 03: "))
    media = (nota1 + nota2 + nota3) / 3 

    print(
        f"O aluno obteve as seguintes notas:",
        f"{nota1}",
        f"{nota2}",
        f"{nota3}",
        f"Obtendo média final de: {media:.2f}",
        sep="\n"
    )
def main():
    calcular_media()
main()