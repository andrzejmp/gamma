def checkTriangle (a, b, c):
	result = False    
	if ((a<b+c) and (b<a+c) and (c<a+b)):
		result = True
	return result

def my_power(a,n):
	result = 1
	for i in range(n):
		result *= a
	return result

def fibo(n):
	if n == 1: return 1 
	if n == 2: return 1 
	return fibo(n-1) + fibo(n-2)
	

