# 26. Cálculo de Média
# - Crie uma lista chamada notas com as notas de 5 alunos fornecidas pelo usuário.
# - Use um laço for para calcular a média das notas.
# - Exiba a média no final.

listaNotas =[]

for i in range(0,5):
    listaNotas.append(float(input("Digite uma nota:\n")))

soma = 0

for nota in listaNotas:
    soma+=nota

media = soma/len(listaNotas)

print(f"A média dos alunos foi: {media}")