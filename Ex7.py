num1 = float(input("Escreva o primeiro valor: "))
num2 = float(input("Escreva o segundo valor: "))

print("1 ou '+' - Adição")
print("2 ou '-' - Subtração")
print("3 ou '*' - multiplicação")
print("4 ou '/' - divisão")
choice = str(input("Escolha uma operação: "))

if choice=="1" or choice=="+":
    print(float(num1)+(num2))
if choice=="2" or choice=="-":
    print(float(num1)-(num2))
if choice=="3" or choice=="*":
    print(float(num1)*(num2))
if choice=="4" or choice=="/":
    print(float(num1)/(num2))