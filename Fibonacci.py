def Fibonacci_num(n):
	if n <= 1:
		return n
	else:
		nth_num = Fibonacci_num(n - 1) + Fibonacci_num(n - 2)
	return nth_num

while True:
	n = int(input("Enter a number greater than 0:"))
	if n >= 0:
		break

print(Fibonacci_num(n))
