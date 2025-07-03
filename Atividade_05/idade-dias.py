from datetime import date

def calcular_idade_dias(data_nascimeto):
    hoje = date.today()
    idade_dias = (hoje - data_nascimeto).days
    return idade_dias

ano = int(input("Ano de nascimeto: "))
mes = int(input("Mês de nascimento: "))
dia = int(input("Dia de nascimento: "))

data_nasc = date(ano, mes, dia)
dias = calcular_idade_dias(data_nasc)
print(f"Você tem {dias} dias de vida.")