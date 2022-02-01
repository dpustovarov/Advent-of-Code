import sys, statistics

def solution(N):
    m = int(statistics.median(N))
    return sum(abs(n - m) for n in N)

print(solution([int(n) for n in sys.stdin.read().split(',')]))
