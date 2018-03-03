import sys
def formingMagicSquare(s):
    k = 0
    a = s[0][0]+s[0][1]+s[0][2]
    b = s[1][0]+s[1][1]+s[1][2]
    c = s[2][0]+s[2][1]+s[2][2]
    d = s[0][0]+s[1][0]+s[2][0]
    e = s[2][0]+s[1][1]+s[0][2]
    f = s[0][0]+s[1][1]+s[2][2]
    g = s[0][1]+s[1][1]+s[2][1]
    h = s[0][2]+s[1][2]+s[2][2]
    j = [a,b,c,d,e,f,g,h]
    for i in j:
        m = abs(15 - i)
        k = k + m
    return k/2,j
if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
