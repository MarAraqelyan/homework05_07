def digit_sum(num):
	if num == 0:
		return 0
	return num % 10 + digit_sum(num // 10)
while True:
	num = int(input("Enter a positive number:"))
	if num > 0:
		break

print(digit_sum(num))	
