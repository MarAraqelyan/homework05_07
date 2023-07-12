def bubble_sort(ls):
	l = len(ls)
	for i in range(l - 1):
		swap = False
		for j in range(l - 1 - i):
			if ls[j] > ls[j + 1]:
				ls[j], ls[j + 1] = ls[j + 1], ls[j]
				swap = True
		if swap == False:
			break
	return ls

ls = [45, 6, 32, 8, 10, 23, 1, 24, 7]
print(bubble_sort(ls))
