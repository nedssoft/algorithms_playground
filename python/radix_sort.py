
from typing import List

def get_num_digits(arr: List[int]) -> int:
    m = 0
    for num in arr:
      m = max(m, num)
    return len(str(m))
def flatten(items: List[int]) -> List[int]:
  ans = []
  for item in items:
    ans = ans + item
  return ans

def radix_sort(arr: List[int]) -> List[int]:
  
  num_digits = get_num_digits(arr)
  for digit in range(num_digits):
    B = [[] for _ in range(10)]
    for item in arr:
      idx = item // 10 ** digit % 10
      B[idx].append(item)
    arr = flatten(B)
  return arr

arr = [i for i in range(1, 10000001)]
from random import shuffle
shuffle(arr)
R = radix_sort(arr)
print(R[:6], R[-6:])
# [1, 2, 3, 4, 5, 6] [9999995, 9999996, 9999997, 9999998, 9999999, 10000000]
    