#!/bin/python3

import sys
def leftrackfall(n,height,position):
    i = n-1
    j = n-2
    while position[j]+height[j]>=position[i]:
        if j == 0:
            return False
        else:
            i = i -1
            j = j -1
    return True
def rightrackfall(n,height,position):
    i = 1
    j = 0
    while position[i] - height[i] <=position[j]:
        if i == n-1:
            return False
        else:
            i = i+1
            j = j+1
    return True
def checkAll(n, height, position):
    # Complete this function
    if leftrackfall(n,height,position) and rightrackfall(n,height,position):
        print('NONE')
    elif not leftrackfall(n,height,position) and not rightrackfall(n,height,position):
        print('BOTH')
    elif not rightrackfall(n,height,position):
        print('LEFT')
    elif not leftrackfall(n,height,position):
        print('RIGHT')

if __name__ == "__main__":
    n = int(input().strip())
    position = list(map(int, input().strip().split(' ')))
    height = list(map(int, input().strip().split(' ')))
    checkAll(n, height, position)
