str1 = input().lower()
a = list(str1)
b = a[:]
a.reverse()
if a==b:
    print('YES')
else:
    print("NO")
