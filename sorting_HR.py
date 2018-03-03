#!/bin/python3

import sys

def bigSorting(arr):
    arr.sort(key=int)
    for i in arr:
        print(i)

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    bigSorting(arr)
    


