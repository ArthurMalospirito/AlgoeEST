usuario=input("defina o usuário\n")
senha=input("defina a senha\n")

if  len(senha)>= 8:
    print("senha definida")

else:
    print("a senha deve conter no mínimo 8 caracteres")
    senha=input("defina a senha\n")

usuariocorreto = usuario.lower()

usuariologin=input("defina o usuário\n")
senhalogin=input("defina a senha\n")

if usuariologin==usuario:

    if senhalogin==senha:

        print("login efetuado")

    else:
        print("senha incorreta, insira novamente")
        senhalogin=input("defina a senha\n")
else:
    print("usuário incorreto, insira novamente")
    usuariologin=input("defina o usuário\n")




    
 