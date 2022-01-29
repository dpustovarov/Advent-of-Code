import sys, collections

def solution(L):
    P = collections.defaultdict(int)
    for (x1, y1), (x2, y2) in L:
        if x1 == x2: 
            for y in range(y1, y2+1) if y1 < y2 else range(y2, y1+1): 
                P[x1, y] += 1

        if y1 == y2: 
            for x in range(x1, x2+1) if x1 < x2 else range(x2, x1+1): 
                P[x, y1] += 1

    return sum(p > 1 for p in P.values())


print(solution(((int(n) for n in p.split(',')) for p in s.split('->')) for s in sys.stdin.readlines()))
