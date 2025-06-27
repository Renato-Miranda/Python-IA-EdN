def conversor_temp():
    origem = input("Converter dê: ")
    temperatura = float(input("Digite a temperatura: "))
    destino = input("Converte para: ")

    fahrenheit = 0
    celcius = 0
    kelvin = 0

    if origem == "c" and destino == "f":
        celcius = temperatura
        fahrenheit = (celcius * 9/5) + 32
        print(fahrenheit)


conversor_temp()