a = int(input("Digite o primeiro número\n> "))
b = int(input("Digite o segundo número\n> "))

mdc = 1

if a <= b:

	for i in range(1,a+1):
		if a%i==0 and b%i==0:
			mdc = i 
else:
	for x in range(1,b+1):
		if a%x==0 and b%x==0:
			mdc = x 	

print("O máximo Divisor Comum (MDC) é: {}".format(mdc))