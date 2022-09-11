"""
In computer graphics, an uncompressed raster image is presented as a matrix of numbers. 
Each entry of the matrix represents the color of a pixel. 
A flood fill algorithm takes a coordinate, r, c, and replaces all pixels connected to r, c 
that have the same color as r, c with the replacement color. 
An example of this is MS-Paint’s paint bucket tool.
"""

from typing import List, Tuple

def flood_fill(image: List[List[int]], start: Tuple[int, int], replacement_color: int) -> None:

  num_rows = len(image)
  num_cols = len(image[0])

  def get_neighbors(cord):
    res = []
    row_delta = [-1, 0, 1, 0]
    col_delta = row_delta[::-1]
    row, col = cord
    r, c = start
    for i in range(len(row_delta)):
      n_row = row + row_delta[i]
      n_col = col_delta[i] + col

      if 0<= n_row < num_rows and 0<= n_col < num_cols:
        if image[r][c] != image[n_row][n_col]: continue
        res.append((n_row, n_col))
    return res

  from collections import deque
  def bfs(root):
    q = deque([root])
    visited = set()
    matches = []
    while q:
      node = q.popleft()
      if node in visited: continue
      for neighbor in get_neighbors(node):
        matches.append(neighbor)
        q.append(neighbor)
      visited.add(node)
    for x, y in matches:
      image[x][y] = replacement_color
  bfs(start)


#Driver code
inputs =  ["2 2","1 1"]
inputs1 = ["9", "9"]
inputs2 = ["5", "4"]
inputs3 = [
    ["0 1 3 4 1","3 8 8 3 3","6 7 8 8 3","12 2 8 9 1","12 3 1 3 2"],
    ["0 1 6 4","2 3 3 5","3 3 3 3","6 4 3 4"]
]
expected_outputs = [
    ["0 1 3 4 1","3 9 9 3 3","6 7 9 9 3","12 2 9 9 1","12 3 1 3 2"],
    ["0 1 6 4","2 9 9 5","9 9 9 9","6 4 9 4"]
]
for i in range(len(inputs)):
    start = tuple(int(x) for x in inputs[i].split())
    color = int(inputs1[i])
    image = [];
    for j in range(int(inputs2[i])):
        image.append([int(x) for x in inputs3[i][j].split()])
    flood_fill(image, start, color);
    actual_output =[]
    for row in image:
        actual_output.append(' '.join(str(x) for x in row))
    print("Flood fill : ",actual_output)