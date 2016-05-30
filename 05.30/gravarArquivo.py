

alunos = []
continua = "s"
while continua == "s":
    matricula = input("Matricula:")
    nome = input("Nome do aluno:")
    cpf = input("CPF:")
    alunos.append([matricula,cpf,nome])
    continua = input("Continua?[s/n]")

arquivo = open("alunos.txt","a")
for aluno in alunos:
    arquivo.write("%s;%s;%s\n" % (aluno[0],aluno[1],aluno[2]))
arquivo.close()
