def binary_search_recursive(array, target, low, high):
	if low > high:
		return -1
	mid = (high + low) // 2
	if array[mid] == target:
		return mid
	elif array[mid] < target:
		return binary_search_recursive(array, target, mid + 1, high)
	elif array[mid] > target:
		return binary_search_recursive(array, target, low, mid - 1)

array = [1, 2, 4, 6, 15, 20, 21]
target = int(input("Enter the target:"))

target_index = binary_search_recursive(array, target, 0, len(array) - 1)
if target_index != -1:
	print("The target is at index", target_index)
else:
	print("Target isn't found in the array")
