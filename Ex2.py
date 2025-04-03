loginCerto = "admin"
senhaCerta = "1234"

login = input("Digite seu Login:\n")
senha = input("Digite sua senha:\n")

if login==loginCerto:
    if senha==senhaCerta:
        print("Login efetuado com sucesso")
    else:
        print("Senha incorreta")
else:
    print("login incorreto")