#!/usr/bin/python

def printNSteps(n:int, msg: str) -> None:
    for i in range(n):
        print(msg)

def displayPathtoPrincess(n,grid):
#print all the moves here
    steps : int = n // 2
    if grid[0][0] == 'p':
        printNSteps(steps, 'UP')
        printNSteps(steps, 'LEFT')
    elif grid[n-1][n-1] == 'p':
        printNSteps(steps, 'DOWN')
        printNSteps(steps, 'RIGHT')
    elif grid[0][n-1] == 'p':
        printNSteps(steps, 'UP')
        printNSteps(steps, 'RIGHT')
    elif grid[n-1][0] == 'p':
        printNSteps(steps, 'DOWN')
        printNSteps(steps, 'LEFT')



m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)