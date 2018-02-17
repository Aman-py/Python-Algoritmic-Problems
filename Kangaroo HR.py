import sys

def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1 ==x2:
        print('YES')
    elif v1>v2:
        if x2>x1:
            if (x2-x1)%(v2-v1)==0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    elif v2<v1:
        if x1>x2:
            if (x2-x1)%(v2-v1)==0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
        

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
kangaroo(x1, v1, x2, v2)
