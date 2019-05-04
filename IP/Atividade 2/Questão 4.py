nome = input("Digite seu nome.\n>")
nome = nome.split()

nome[0] = nome[0].upper()
nome[len(nome)-1] =  nome[len(nome)-1].upper()

print(" ".join(nome))