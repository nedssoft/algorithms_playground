from collections import deque

"""
On an infinitely large chessboard, a knight is located on [0, 0].
A knight can move in eight directions.
Given a destination coordinate [x, y], determine the minimum number of moves from [0, 0] to [x, y].

Pseudo code:

- Create a function to get coordinate neighbors, not that the chessboard is infinite, hence, no need to check grid boundary
- Create a BFS function to transverse the chessboard, 
- Create a visited set to marked visited cordinate
- Create a step variable to hold the number of steps
- for each neighbor, check if it's same as the target cordinate (x, y), return step
"""
def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(node):
        dx = [-2,-2,1,-1,1,2,2,1,-1]
        dy = dx[::-1]
        row, col = node
        neighbors = []
        for i in range(len(dx)):
            r, c = dx[i] + row, dy[i] + col
            neighbors.append((r, c))
        return neighbors
    
    def bfs(root):
        q = deque([root])
        visited = set()
        step = 0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node == (x, y):
                    return step
                if node in visited: continue
                for ne in get_neighbors(node):
                    q.append(ne)
                visited.add(node)
            step += 1
    return bfs((0,0))

#Driver code
inputs = ["2 1", "5 5"]
for i in range(len(inputs)):
    x, y = [int(x) for x in inputs[i].split()]
    print("Get knight shortest path :",get_knight_shortest_path(x, y))