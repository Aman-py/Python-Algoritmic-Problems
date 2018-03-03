#!/bin/python3

import sys

def maximumSum(a, m):
    l = []
    for i in range(len(a)):
        for j in range(1,len(a)):
            if i - j != 0:
                k = sum(a[i:j])%m
                l.append(k)
    return print(max(l))
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        a = list(map(int, input().strip().split(' ')))
        maximumSum(a, m)
        
