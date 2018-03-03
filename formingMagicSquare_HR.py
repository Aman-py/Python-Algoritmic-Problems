import sys

def formingMagicSquare(s):
    a = 0
    m = [2,4,6,8]
    n = [1,3,7,9]
    p = [s[0][0],s[0][2],s[2][0],s[2][2]]
    q = [s[0][1],s[1][2],s[2][1],s[1][0]]
    if s[1][1] != 5:
        a = abs(5-s[1][1])
    for i in range(4):
        x = abs(max(m)-max(p))
        a = a+x
        m.remove(max(m))
        p.remove(max(p))
        y = abs(max(n)-max(q))
        a = y+a
        n.remove(max(n))
        q.remove(max(q))
    return int(a)
if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
