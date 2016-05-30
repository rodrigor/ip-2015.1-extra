
arquivo = open("alunos.txt","r")
linhas = arquivo.read().splitlines()
arquivo.close()

for linha in linhas:
    aluno = linha.split(";")
    print("Matricula: %s" % aluno[0])
    print("CPF: %s" % aluno[1])
    print("Nome: %s" % aluno[2])
