def binary_search_iterative(array, target, low, high):
	while high > low:
		mid = (low + high) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			high -= 1
		elif array[mid] < target:
			low += 1
	return -1

ls = [0, 2, 4, 5, 8, 9, 10]
target = int(input("Enter the target:"))
target_index = binary_search_iterative(ls, target, 0, len(ls) - 1)

if target_index != -1:
	print("The target is at index", target_index)
else:
	print("Target not found in list")
		
