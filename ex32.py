

def tabuadaPersonalisada(base,inicio,fim):
    print(f"tabuada do:{base} de {inicio} a {fim}:")
    for j in range(inicio,fim+1):
        print(f"{base} x {j} = {base*j}")
    print()#espaço extra para separar as tabuadas

valorTabuada = int(input("Digite o valor para saber tabuada:\n"))
inicioTabuada = int(input("Digite o valor inicial da sua tabuada:\n"))
fimTabuada = int(input("Digite o valor final da sua tabuada:\n"))

tabuadaPersonalisada(valorTabuada,inicioTabuada,fimTabuada)