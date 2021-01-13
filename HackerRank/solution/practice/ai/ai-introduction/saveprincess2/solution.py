#

def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                if i == r:
                    if j < c:
                        return 'LEFT'
                    else:
                        return 'RIGHT'
                if j == c:
                    if i < r:
                        return 'UP'
                    else:
                        return 'DOWN'
                if i < r:
                    return 'UP'
                else:
                    return 'DOWN'
                    

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))