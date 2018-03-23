n = int(input())
arr = [int(temp) for temp in input().strip().split(' ')]
answer = 1
for i in arr:
    answer = (answer*i)%(10**9+7)
print(answer)
