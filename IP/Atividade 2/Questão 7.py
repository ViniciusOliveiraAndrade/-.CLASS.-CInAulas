qt = int(input("Digite a quantidade de alunos.\n>"))

lista = []

for i in range(qt):
	lista.append(int(input("Digite a nota do {}° aluno.\n>".format(i+1))))

media = sum(lista)/len(lista)
print("A média é: {}".format(media))

for j in lista:
	if j > media:
		print("Nota maior que a média: {}".format(j))