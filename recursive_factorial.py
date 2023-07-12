cache = {}
def factorial_rec(n):
	if n < 2:
		return 1
	if n in cache:
		return cache[n]
	else:
		cache[n] = n * factorial_rec(n - 1)
	return cache[n]
while True:
	num = int(input("Enter a non-negative number:"))
	if num >= 0:
		break
factorial = factorial_rec(num)
print(factorial)	
	

