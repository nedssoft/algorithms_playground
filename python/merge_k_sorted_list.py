from typing import List
from heapq import heappush, heappop

def merge_k_sorted_list(lists: List[List[int]]) -> List[int]:

  heap = []
  res = []
  for curr in lists:
    heappush(heap, (curr[0], curr, 0))
  
  while heap:
    val, curr, i = heappop(heap)
    res.append(val)
    i += 1
    if i < len(curr):
      heappush(heap, (curr[i], curr, i))
  return res

if __name__ == '__main__':
  print(merge_k_sorted_list([[1,4,5],[1,3,4],[2,6]]))
