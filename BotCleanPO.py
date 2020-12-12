#!/usr/bin/python

# Head ends here
import math
from typing import Tuple
from random import random
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

def max_unknown(posr: int,posc: int, board, n: int) ->Tuple[int, int]:
    maxdist = 0.0
    point = (posr,posc)
    robot = (posr,posc)
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'o':
                p = (row,col)
                d = dist(robot, p)
                if d > maxdist or ( d == maxdist and random() > 0.5):
                    maxdist = d
                    point = p
    return point

def exec(posr, posc, row, col):
    if row == posr and col == posc:
        print("CLEAN")
    elif row < posr :
        print("UP")
    elif row > posr:
        print("DOWN")
    elif col < posc:
        print("LEFT")
    else:
        print("RIGHT")

def scan(posr, posc) -> str:
    strategy = [
        ["RIGHT",  "DOWN", "DOWN", "DOWN","DOWN"],
        ["RIGHT",  "RIGHT","RIGHT","DOWN", "LEFT"],
        ["RIGHT",   "UP",  "DOWN", "DOWN", "LEFT"],
        ["RIGHT",   "UP",  "LEFT", "LEFT", "LEFT"],
        ["UP",      "UP",  "UP",   "UP",   "LEFT"],
    ]
    return strategy[posr][posc]

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print('CLEAN')
    else:
        pn = nearest(posr, posc, board, 5)
        if not pn is None:
            (row, col) = pn
            exec(posr, posc, row, col)
        else:
            print(scan(posr, posc))

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)