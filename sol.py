inp = input();

inps = inp.split(' ')

x = inps[0]

y = inps[1]



def gcd(a, b):
	if(b == 0):
		return a;
	else:
		return gcd(b, a%b);


print (gcd(int(x),int(y)));