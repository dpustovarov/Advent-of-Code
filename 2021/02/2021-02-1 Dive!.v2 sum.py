import sys

def solution(C):
    return sum(n for d, n in C if d == 'f') * (sum(n for d, n in C if d == 'd') - sum(n for d, n in C if d == 'u'))

print(solution([(d[0], int(n)) for d, n in (s.split(' ') for s in sys.stdin.readlines())]))
