# Validação de número (1 a 10)
while True:
    try:
        numero = int(input("Digite um número de 1 a 10: "))
        if 1 <= numero <= 10:
            print("Número válido!")
            break
        else:
            print("Número inválido! Tente novamente.\n")
    except ValueError:
        print("Por favor, digite um número inteiro válido.\n")
