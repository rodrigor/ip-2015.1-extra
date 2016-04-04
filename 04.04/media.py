
nomes = []
medias = []

for i in range(5):
    nomes.append(input("Digite seu nome:"))
    medias.append(float(input("Digite a média:")))

for i in range(len(nomes)):
    media = medias[i]
    nome = nomes[i]
    if media >= 7:
        print(nome,"foi APROVADO(A)")
    elif media >= 4:
        print(nome,"está na FINAL!")
    else:
        print(nome,"foi REPROVADO(A)")
