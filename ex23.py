# 23. Tabuada com Vetores
# - Peça ao usuário para digitar um número inteiro.
# - Crie uma lista chamada tabuada que contenha os resultados da tabuada desse número (1 a 10).
# - Use o laço for para preencher a lista com os resultados e depois exiba os valores armazenados.

numero = int(input("Digite um número inteiro:\n"))

tabuada = []

for i in range(1,11):
    tabuada.append(numero*i)

for i in tabuada:
    print(i)