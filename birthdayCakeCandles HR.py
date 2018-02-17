#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    a =0
    for i in range(len(ar)):
        if ar[i] == max(ar):
            a = a+1
    return print(a)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
birthdayCakeCandles(n, ar)
