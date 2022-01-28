import sys, collections

def solution(D, L):
    l, m, n = len(L), len(L[0]), len(L[0][0])
    row = [[n] * m for _ in range(l)]
    col = [[m] * n for _ in range(l)]
    unmarked = [sum(map(sum, M)) for M in L]

    num = collections.defaultdict(list)
    for k, M in enumerate(L):
        for i, R in enumerate(M):
            for j, N in enumerate(R): 
                num[N].append((k, i, j))

    finished = set()
    for d in D:
        for k, i, j in num[d]:
            if k in finished: continue

            row[k][i] -= 1
            col[k][j] -= 1
            unmarked[k] -= d
            
            if row[k][i] == 0 or col[k][j] == 0: 
                finished.add(k)
                if len(finished) == l: return d * unmarked[k]

print(solution(map(int, sys.stdin.readline().split(',')), [[[int(c) for c in s.split()] for s in b.splitlines() if s] for b in sys.stdin.read().split('\n\n')]))
