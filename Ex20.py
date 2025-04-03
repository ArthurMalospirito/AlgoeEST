idade = int(input("Digite sua idade:\n"))
menbro = input("Você é menbro do clube? (Sim/Nao)\n").lower()
acompanhando =input("Você está acompanhando algum menbro? (Sim/Nao)\n")

if idade>=18:
    if menbro=="sim":
        print("Você pode entrar")
    elif acompanhando=="sim":
        print("Você deve pagar meia entrada")
    else:
        print("Você deve pagar um ingresso")
else:
    print("Você não pode entrar, você deve ser maior de 18 anos")