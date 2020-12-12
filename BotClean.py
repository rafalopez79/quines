#!/usr/bin/python

# Head ends here
import math
from typing import Tuple
import sys

def dist(x:Tuple[int, int], y: Tuple[int, int]) -> float:
    a = x[0] - y[0]
    b = x[1] - y[1]
    return math.sqrt(a*a + b*b)

def nearest(posr: int,posc: int, board, n: int) ->Tuple[int, int]:
    mindist = sys.maxsize
    minpoint = None
    robot = (posr,posc)
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'd':
                p = (row,col)
                d = dist(robot, p)
                if d < mindist:
                    mindist = d
                    minpoint = p
    return minpoint

def next_move(posr, posc, board):
    pn = nearest(posr, posc, board, 5)
    if pn is None:
        print("")
    else:
        (row, col) = pn
        if row == posr and col == posc :
            print("CLEAN")
        elif row < posr :
            print("UP")
        elif row > posr:
            print("DOWN")
        elif col < posc:
            print("LEFT")
        else:
            print("RIGHT")

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)