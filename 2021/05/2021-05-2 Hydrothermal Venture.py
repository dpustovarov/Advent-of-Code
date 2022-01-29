import sys, collections

def solution(L):
    P = collections.defaultdict(int)
    for (x, y), (x2, y2) in L:
        P[x, y] += 1

        dx, dy = (x2 > x) - (x2 < x), (y2 > y) - (y2 < y)   # cmp
        while x != x2 or y != y2:
            x += dx; y += dy
            P[x, y] += 1

    return sum(p > 1 for p in P.values())


print(solution(((int(n) for n in p.split(',')) for p in s.split('->')) for s in sys.stdin.readlines()))
