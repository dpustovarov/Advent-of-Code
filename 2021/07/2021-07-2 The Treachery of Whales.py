import sys, statistics

def solution(N):
    m = int(round(statistics.mean(N)))  # average for (n - i)**2
    d = int(statistics.median(N))       # average for abs(n - i)
    return min(sum((n - i)**2 + abs(n - i) for n in N) for i in range(m, d, (d > m) - (d < m))) // 2

print(solution([int(n) for n in sys.stdin.read().split(',')]))
