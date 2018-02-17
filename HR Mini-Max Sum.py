#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    a = 0
    for i in range(len(arr)):
        a = a+arr[i]
    return print(a-max(arr),a-min(arr))    

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
