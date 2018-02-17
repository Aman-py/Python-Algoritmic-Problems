#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr1 = []
i = len(arr)-1
while i >=0:
    a = arr[i]
    arr1.append(a)
    i-=1
print(arr1)
