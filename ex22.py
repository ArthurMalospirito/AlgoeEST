# 22. Contando Elementos em uma Lista
# - Crie uma lista chamada palavras com 6 palavras fornecidas pelo usuário.
# - Use um laço for para contar quantas palavras têm mais de 5 caracteres.
# - Exiba o total no final.

palavras = []

for i in range(0,6):
    palavras.append(input("Digite uma palavra nova para ser adicionada:\n"))

qtdMaiorQue5 = 0

for palavra in palavras:
    if len(palavra)>5:
        qtdMaiorQue5+=1

print(f"A quantidade de palavras maiores que 5 letras é {qtdMaiorQue5}")