# 27. Lista de Nomes
# - Crie uma lista chamada nomes e insira os nomes de 5 amigos.
# - Use um laço for para exibir os nomes em ordem alfabética.

listaNomes=[]

for i in range(0,5):
    listaNomes.append(input("Digite o nome de um amigo:\n"))

listaNomes.sort()
print(listaNomes)