def classificar_idade():
    
    try:
        idade = int(input("Digite a idade: "))

        if idade >= 60:
            print("Idoso")
        elif idade >= 18:
            print("Adulto")
        elif idade >= 13:
            print("Adolescente")
        else:
            print("criança")

    except ValueError:
        print("Erro")

classificar_idade()

    