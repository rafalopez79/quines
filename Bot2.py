def find(grid, p, n):
    for row in range(n):
        for col in range(n):
            if grid[row][col] == p:
                return (row, col)
    return None

def nextMove(n,r,c,grid):
    (row, col) = find(grid, 'p', n)
    if row < r :
        return "UP"
    elif row > r:
        return "DOWN"
    elif col < c:
        return "LEFT"
    else:
        return "RIGHT"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))