#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    if grid[n-1][0] == 'p':
        [print('DOWN') for _ in range(n//2)]
        [print('LEFT') for _ in range(n//2)]
    elif grid[0][0] == 'p':
        [print('UP') for _ in range(n//2)]
        [print('LEFT') for _ in range(n//2)]
    elif grid[0][n-1] == 'p':
        [print('UP') for _ in range(n//2)]
        [print('RIGHT') for _ in range(n//2)]
    elif grid[n-1][n-1] == 'p':
        [print('DOWN') for _ in range(n//2)]
        [print('RIGHT') for _ in range(n//2)]
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)