arr = []
while True:
    n = int(input())
    if n != 42:
        arr.append(n)
    if n == 42:
        j = int(input())
        break
for i in arr:
    print(i)
