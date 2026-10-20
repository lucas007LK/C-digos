# Dias da semana e escolha de treino
dias_da_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

print("\nDias da semana:\n")

for i, dia in enumerate(dias_da_semana, 1):
    print("{} - {}".format(i, dia))

escolha = input("\nEscolha o dia que você quer treinar: ")

for dia in dias_da_semana:
    if escolha.lower() in dia.lower():
        print("\nVocê escolheu treinar na {}!".format(dia))
