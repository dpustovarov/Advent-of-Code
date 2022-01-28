import sys, collections

def solution(D, L):
    row = [[len(L[0][0])] * len(L[0]) for _ in range(len(L))]
    col = [[len(L[0])] * len(L[0][0]) for _ in range(len(L))]
    unmarked = [sum(map(sum, M)) for M in L]

    num = collections.defaultdict(list)
    for k, M in enumerate(L):
        for i, R in enumerate(M):
            for j, N in enumerate(R): 
                num[N].append((k, i, j))

    for d in D:
        for k, i, j in num[d]:
            row[k][i] -= 1
            col[k][j] -= 1
            unmarked[k] -= d
            
            if row[k][i] == 0 or col[k][j] == 0: return d * unmarked[k]


D = map(int, sys.stdin.readline().split(','))
L = []
for s in sys.stdin.readlines():
    if s.strip(): 
        L[-1].append([int(c) for c in s.split(' ') if c])
    else:
        L.append([])

print(solution(D, L))
