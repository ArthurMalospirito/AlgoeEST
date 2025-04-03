produto = input("Digite o produto a ser comprado\n")
qtd = int(input("Digite a quantidade que irá comprar\n"))
precoUnidade = float(input("Digite o preço da unidade do produto\n"))

precoTotal = precoUnidade*qtd

if precoTotal>100:
    precoTotal=precoTotal*0.95

print(f"Total: R$ {precoTotal}")