#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    for i in range(n+1):
        j = n-i
        print(j*' '+i*'#')

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
