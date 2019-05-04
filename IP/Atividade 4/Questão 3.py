def cal(a,b,x=1,i=1):
	if i > a:
		return x
	else:
		if a%i==0 and b%i==0:
			x = i
		return cal(a,b,x,i+1)

def MDC(a,b):
	if a <= b:
		mdc = cal(a,b)
	else:
		mdc = cal(b,a)
	return mdc


def div(n,i=1):
	print(n)
	print(i)

	if i > n-1:
		print()
		return i
	elif n % i != 0:
		print(n)
		print(i)

		return div(n,i+1)

def PRIMO(n):
	if div(n) != n:
		print("O número '{}' nao é primo".format(n))
	else:
		print("O número '{}' é primo".format(n))


#for i in range(1,1002):
#	PRIMO(i)

PRIMO(7)





def som(n,s=0,i=1):
	if i > n-1:
		return s
	else:
		if n % i == 0:
			s+=i
		return som(n,s,i+1)

def PERFEITO(n):
	if som(n) == n:
		print("O número ' {} ' é perfeito".format(n))
	else:
		print("O número ' {} ' nao é perfeito".format(n))

