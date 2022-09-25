from typing import List
def merge_sort(arr: List[int]):
	if len(arr) <= 1: return
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	
	merge_sort(left)
	merge_sort(right)
	
	i = j = k = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1

arr = [2, 3,5,1, 1,1, 7,4,4,4,2,6,0]

merge_sort(arr)

print(arr)
      