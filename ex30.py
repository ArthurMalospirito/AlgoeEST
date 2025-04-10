# 30. Encontrando Palíndromos
# - Crie uma lista chamada palavras com 5 palavras fornecidas pelo usuário.
# - Use um laço for para verificar quais palavras são palíndromos (ou seja, que podem ser lidas da mesma forma de trás para frente, como "arara").
# - Exiba as palavras palíndromas no final.

palavras=[]

for i in range(0,5):
    palavras.append(input("Digite uma palavra:\n"))

palavraReverse=""
palavrasPalindromos=[]

for palavra in palavras:
    palavraNormal=palavra[::-1]
    if palavraNormal==palavra:
        palavrasPalindromos.append(palavra)

if len(palavrasPalindromos)==0:
    print("Você não digitou nenhum palindromo")
else:
    print(f"As palavras que são palindromos são: {palavrasPalindromos}")