n = int(input())
for i in range(n):
    str1,str2 = [temp for temp in input().strip().split(' ')]
    if len(str1) != len(str2):
        print('NO')
    elif len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] in str2 and str2[i] in str1:
               j = 0 
            if str1[i] not in str2 or str2[i] not in str1:
                print('NO')
                break
        print('YES')
               
