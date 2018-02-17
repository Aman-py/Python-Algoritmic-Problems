#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    a=0
    for i in range(len(ar)):
       a = a+ar[i]
    return print(a)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
aVeryBigSum(n, ar)
