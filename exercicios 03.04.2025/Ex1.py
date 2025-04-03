nomeAluno = input("Digite seu nome:\n")
idadeAluno = int(input("Digite sua Idade:\n"))
turmaAluno = input("Digite sua turma:\n")

if idadeAluno>=6:      
    print(f"Aluno cadastrado com sucesso: {nomeAluno}, {idadeAluno} Anos, {turmaAluno}")
else:
    print("Você deve ser maior que 6 anos, Cadastro falho.")
    