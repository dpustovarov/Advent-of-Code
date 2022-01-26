import sys

def solution(C):
    x = y = aim = 0
    for d, n in C:
        if d == 'f': 
            x += n; y += aim * n
        elif d == 'd':
            aim += n
        elif d == 'u':
            aim -= n

    return x * y
 
C = []
for s in sys.stdin.readlines():
    d, n = s.split(' ')
    C.append((d[0], int(n)))
print(solution(C))
