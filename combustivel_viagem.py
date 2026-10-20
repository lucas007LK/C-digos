# Cálculo de combustível gasto em viagem
tempo = int(input("Digite o tempo gasto (horas): "))
velocidade = int(input("Digite a velocidade média (km/h): "))

distancia = tempo * velocidade
litros = distancia / 12

print(f"{litros:.3f}")
