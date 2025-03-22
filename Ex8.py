LoginCerto = "Arthur"
SenhaCerta = "12345"
Login = ""
Senha = ""


Login = str(input("Escreva o login: "))
Senha = str(input("Escreva a senha: "))

if Login==LoginCerto:
    if Senha==SenhaCerta:
        print("Acesso concedido")
    else:
        print("Senha incorreta")
else:
    print("Login incorreto")