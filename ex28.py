# 28. Filtrando Números Pares e Ímpares
# - Crie uma lista chamada numeros com 8 números inteiros escolhidos pelo usuário.
# - Use um laço for para dividir os números em duas listas: pares e impares.

listaValores =[]

for i in range(0,8):
    listaValores.append(int(input("Digite um valor inteiro:\n")))

listaPares=[]
listaImpares=[]

for valor in listaValores:
    if valor%2==0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)
    
print(f"Os itens pares foram: {listaPares}")
print(f"Os itens impares foram: {listaImpares}")