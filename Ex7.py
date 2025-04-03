
genero =input("Digite seu Genero (Masculino/Feminino):\n").lower()
idade = int(input("Digite sua idade:\n"))
atleta = input("Digite se você é atleta (Sim/não)").lower()

if idade>=15:
    if genero=="feminino":
        if idade<=35:
            if idade>=22:
                print("oferecer artigos esportivos e itens de casa")
            else:
                print("oferecer maquiagem e moda")
        else:
            print("Não está na margem de idades")
    else:
        if idade<=32:
            if atleta=="sim":
                print("oferecer artigos esportivos")
            else:
                if idade>=21:
                    print("oferecer livros, jardinagem e eletrodomesticos")
                else:
                    print("Oferecer videogames")
        else:
            print("Não está na margem de idades")
else:
    print("Oferecer artigos infantís")