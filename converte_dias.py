# Conversão de dias totais em anos, meses e dias
dias_totais = int(input("Digite a quantidade de dias: "))

anos = dias_totais // 365
resto = dias_totais % 365

meses = resto // 30
dias = resto % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
