def conversor_temp():
    origem = input("Qual a unidade de medida você quer converter: ")
    temperatura = float(input("Digite a temperatura a ser convetida: "))
    destino = input("Para qual unidade de medida você que seja convertido: ")

    fahrenheit = 0
    celcius = 0
    kelvin = 0
    #celsius para:
    if origem == "c" and destino == "f":
        celcius = temperatura
        fahrenheit = (celcius * 9/5) + 32
        print(f"{fahrenheit:.2f}")
    elif origem == "c" and destino == "k":
         celcius = temperatura
         kelvin = celcius + 273.15
         print(f"{kelvin:.2f}")
    #Fahrenheit para:
    elif origem == "f" and destino == "c":
        fahrenheit = temperatura
        celcius = (fahrenheit - 32) * 5/9
        print(f"{celcius:.2f}")
    elif origem == "f" and destino == "k":
        fahrenheit = temperatura
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f"{kelvin:.2f}")
    #Kelvin para:
    elif origem == "k" and destino == "c":
        kelvin = temperatura
        celcius = kelvin - 273.15
        print(f"{celcius:.2f}")
    elif origem == "k" and destino == "f":
        kelvin = temperatura
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(F"{fahrenheit:.2f}")
    else:
        print("Algo de errado não está certo!!!")



conversor_temp()