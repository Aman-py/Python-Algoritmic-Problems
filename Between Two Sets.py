#!/bin/python3

import sys
def devide(a,i):
	j = 0
	while j<len(a):
		if i%a[j] == 0 and a[j] != 1:
			j = j + 1
		elif i%a[j] != i:
                        return False
		else:
			return False
	return True
def devide1(b,i):
	j = 0
	while j<len(b):
		if b[j]%i == 0:
			j = j + 1
		else:
			return False
	return True

def getTotalX(a, b):
    j = 0
    for i in range(1,max(b)):
        if devide1(b,i) and devide(a,i):
            j = j+1
    print(j)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    getTotalX(a, b)
    

