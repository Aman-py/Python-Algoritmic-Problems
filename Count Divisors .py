l,r,k = [int(temp) for temp in input().strip().split(' ')]
m = 0
for i in range(l,(r+1)):
    if i%k==0:
        m+=1
print(m)
