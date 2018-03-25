n,q = [int(temp) for temp in input().split(' ')]
arr = [int(temp) for temp in input().split(' ')]
for i in range(q):
    p,q,r =[int(temp) for temp in input().split(' ')]
    if p ==1:
        arr[q] = r
    if p == 2:
        print(sum(arr[q:(r+1)]))
