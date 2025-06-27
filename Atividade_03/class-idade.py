def classificar_idade():
    idade = int(input("Digite a idade: "))

    if idade >= 60:
        print("Idoso")
    elif idade >= 18:
        print("Adulto")
    elif idade >= 13:
        print("Adolescente")
    else:
        print("criança")

classificar_idade()