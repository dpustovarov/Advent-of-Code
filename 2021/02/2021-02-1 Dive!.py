import sys

def solution(C):
    x = y = 0
    for d, n in C:
        if d == 'f': 
            x += n
        elif d == 'd':
            y += n
        elif d == 'u':
            y -= n

    return x * y
 
C = []
for s in sys.stdin.readlines():
    d, n = s.split(' ')
    C.append((d[0], int(n)))
print(solution(C))
