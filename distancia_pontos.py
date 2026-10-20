# Cálculo da distância entre dois pontos (Geometria Analítica)
import math

x1, y1 = map(float, input("Digite x1 e y1 separados por espaço: ").split())
x2, y2 = map(float, input("Digite x2 e y2 separados por espaço: ").split())

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"{distancia:.4f}")
