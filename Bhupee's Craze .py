n = int(input())
for i in range(n):
    p = int(input())
    arr =[]
    for i in range(p):
        temp = input()
        arr.append(temp)
    dic = {}
    temp = []
    for i in arr:
        j = 1
        for k in set(i):
            j =j*i.count(k)
        if j>1:
            dic[j] = []
            dic[j].append(i)
        if j == 1:
            temp.append(i)
            
    if len(temp) == len(arr):
        print(temp[-1])
    else:
        print(dic[min(dic.keys())][-1])
