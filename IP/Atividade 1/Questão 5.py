
n = int(input("Digite o valor de n\n> "))
fat = 1
for i in range(2,n+1):
    fat *= i

print("O valor de {}! por 'for' é: {}".format(n,fat))

n = int(input("Digite o valor de n\n> "))
fat = 1
i = 2
while i <= n:
    fat *= i
    i += 1

print("O valor de {}! por 'while' é: {}".format(n,fat))