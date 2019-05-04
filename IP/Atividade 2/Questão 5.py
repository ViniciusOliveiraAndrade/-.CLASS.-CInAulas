n = int(input("Digite o tamanho dos vetores.\n>"))

v1 = []
v2 = []

for i in range(n):
	v1.append(int(input("Digite o primeiro Valor do 1° vetor.\n>")))

for j in range(n):
	v2.append(int(input("Digite o primeiro Valor do 2° vetor.\n>")))

for i,valor in enumerate(v1):
	v2[i] += valor

print(v2)