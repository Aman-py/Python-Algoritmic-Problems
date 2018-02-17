#!/bin/python3

import sys

def solve(alice, bob):
    # Complete this function
    a = 0
    b = 0
    for i in range(len(alice)):
        if alice[i] > bob[i]:
            a +=1
        elif alice[i] < bob[i]:
            b +=1
    return print(a,b)

a0, a1, a2 = input().strip().split(' ')
alice = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
bob = [int(b0), int(b1), int(b2)]
solve(alice,bob)


