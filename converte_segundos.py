# Conversão de segundos totais em horas, minutos e segundos
segundos_totais = int(input("Digite a quantidade de segundos: "))

horas = segundos_totais // 3600
resto = segundos_totais % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")
