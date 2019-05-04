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




