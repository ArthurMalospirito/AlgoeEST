# 24. Encontrando o Maior e o Menor Número
# - Crie uma lista chamada numeros com 5 números inteiros fornecidos pelo usuário.
# - Use um laço for para determinar e exibir o maior e o menor número da lista.

listaValores = []

for i in range(0,5):
    listaValores.append(float(input("Digite um número para adicionar:\n")))

maior=listaValores[0]
menor=listaValores[0]

for numero in listaValores:
    if numero>maior:
        maior=numero
    
    if numero<menor:
        menor=numero

print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")