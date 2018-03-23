n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    set1 = set(str1)
    set2 = set(str2)
    j = 0
    for l in set1:
        if  l not in set2:
            j = j+str1.count(l)
        if l in set2:
            j = j+abs(str1.count(l)-str2.count(l))
    for k in set2:
        if  k not in set1:
            j = j+str2.count(k)
    print(j)
