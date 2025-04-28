


def tabuada(numero):
    print(f"tabuada do:{numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

valorTabuada = int(input("Digite o valor que quer descobrir a tabuada:\n"))
tabuada(valorTabuada)