# 25. Jogo de Adivinhação com Vetores
# - Crie um programa onde o computador sorteia um número entre 1 e 20.
# - Armazene os palpites do usuário em uma lista chamada palpites.
# - Use um laço while para permitir que o usuário continue tentando até acertar.
# - Ao final, exiba todos os palpites que o usuário forneceu.

import random

valorAleatorio=random.randrange(1,21)

palpites=[]

while not valorAleatorio in palpites:
    palpites.append(int(input("Digite um valor para chutar:\n")))
print(f"Você acertou, o número era: {valorAleatorio}")
print(f"Seus palpites foram: {palpites}")