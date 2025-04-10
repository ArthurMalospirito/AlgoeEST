# 29. Multiplicação de Elementos da Lista
# - Crie uma lista chamada valores com 4 números inteiros fornecidos pelo usuário.
# - Peça ao usuário um número adicional e multiplique cada elemento da lista pelo número fornecido, usando um laço for.
# - Exiba os novos valores da lista.

listaValores=[]

for i in range(0,4):
    listaValores.append(int(input("Digite um valor inteiro:\n")))

multiplicador=int(input("Digite um valor para multiplicar todos os outros:\n"))

listaValoresMultiplicados=[]

for valor in listaValores:
    listaValoresMultiplicados.append(valor*multiplicador)

print(f"A lista com valores multiplicado é: {listaValoresMultiplicados}")