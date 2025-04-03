salarioBase = float(input("Digite seu salário:\n"))
horasExtras = int(input("Digite a quantidade de horas extras trabalhadas:\n"))
valorHoraExtra = float(input("Digite o valor da hora extra:\n"))

salarioTotal = salarioBase+(horasExtras*valorHoraExtra)

print(f"Seu salário com as horas extras é de R$ {salarioTotal}")
