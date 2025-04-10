# 21. Criando e Manipulando Listas
# - Crie uma lista chamada numeros com 10 números inteiros escolhidos pelo usuário.
# - Use um laço for para imprimir cada número da lista.
# - Calcule e exiba a soma de todos os números usando outro laço for.

Numeros =[]

lista =[1,2,3,4,5,6,7,8,9,10]

for i in range(0,10):
    Numeros.append(float(input("Digite um valor a ser adicionado:\n")))


for numero in Numeros:
    print(numero)

soma =0

for numero in Numeros:
    soma+=numero

print(f"A soma dos números é{soma}")