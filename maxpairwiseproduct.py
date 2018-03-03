# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 1
for i in range(2):
    result=result*max(a)
    a.remove(max(a))
print(result)
