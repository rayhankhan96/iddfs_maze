def is_valid(x, y, grid, visited):
    rows, cols = len(grid), len(grid[0])
    return (0 <= x < rows and 0 <= y < cols and 
            grid[x][y] == 0 and (x, y) not in visited)

def dls(grid, current, target, depth, visited, path):
    if depth < 0:
        return False
    
    x, y = current
    visited.add((x, y))
    path.append((x, y))

    if current == target:
        return True

    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, grid, visited):
            if dls(grid, (nx, ny), target, depth - 1, visited, path):
                return True

    path.pop()
    visited.remove((x, y))
    return False

def iddfs(grid, start, target, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        if dls(grid, start, target, depth, visited, path):
            print(f"Path found at depth {depth} using IDDFS")
            print("Traversal Order:", path)
            return
    print(f"Path not found at max depth {max_depth} using IDDFS")

# -------- Case 1 --------
grid1 = [
    [0,0,1,0],
    [1,0,0,0],
    [0,1,0,0],
    [1,1,0,1]
]

start1 = (0, 0)
target1 = (2, 3)

iddfs(grid1, start1, target1, 6)

# -------- Case 2 --------
grid2 = [
    [0,1,0],
    [0,1,0],
    [0,1,0]
]

start2 = (0, 0)
target2 = (2, 2)

iddfs(grid2, start2, target2, 6)

