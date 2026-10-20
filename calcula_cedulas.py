# Cálculo de cédulas e notas
valor = int(input("Digite o valor: "))
print(valor)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for nota in cedulas:
    quantidade = valor // nota
    valor %= nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
