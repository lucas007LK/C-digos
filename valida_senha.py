# Validação de senha
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")
    
    if senha != "1234":
        print("Senha incorreta!")
    else:
        print("Senha correta!")
        print("Acesso liberado!")
