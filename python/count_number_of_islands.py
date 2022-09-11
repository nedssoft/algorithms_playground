from typing import List, Tuple

from collections import deque

def count_number_of_islands(grid: List[List[int]]) -> int:
  num_rows = len(grid)
  num_cols = len(grid[0])

  count = 0
  visited = set()

  def get_neighbors(node: Tuple[int, int]):
    row_delta = [-1, 0,1, 0]
    col_delta = row_delta[::-1]
    row, col = node
    res = []
    for i in range(len(row_delta)):
      r = row_delta[i] + row
      c = col_delta[i] + col
     
      if 0 <= r < num_rows and 0 <= c < num_cols:
        if grid[r][c] == 0: continue
        res.append((r, c))
    return res
  def bfs(root: Tuple[int, int]):
    q = deque([root])
    r, c = root
    while q:
      node = q.popleft()
      if node in visited: continue
      for neighbor in get_neighbors(node):
        q.append(neighbor)
      
      visited.add(node)
  
  for i in range(num_rows):
    for j in range(num_cols):

      if (i,j) in visited or grid[i][j] == 0: continue

      bfs((i, j))
      count += 1
  return count


inputs = ["6", "2", "3"]
inputsMatrix = [
    [
        "1 1 1 0 0 0",
        "1 1 1 1 0 0",
        "1 1 1 0 0 0",
        "0 1 0 0 0 0",
        "0 0 0 0 1 0",
        "0 0 0 0 0 0",
    ],
    ["1 0 1", "0 1 0"],
    ["0 0 0", "0 0 0", "0 0 0"],
]
for i in range(len(inputs)):
    grid = [[int(x) for x in inputsMatrix[i][j].split()] for j in range(int(inputs[i]))]
    print("Count number of islands :",count_number_of_islands(grid))