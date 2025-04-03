anoNascimento = int(input("Digite o ano que você nasceu:\n"))
anoAtual = int(input("Digite o ano atual:\n"))
fezNiver = input("Digite se fez aniversário esse ano: (Sim/Nao)\n").lower()

idade = anoAtual-anoNascimento

if fezNiver=="nao":
    idade-=1

print(f"Sua idade é {idade}")