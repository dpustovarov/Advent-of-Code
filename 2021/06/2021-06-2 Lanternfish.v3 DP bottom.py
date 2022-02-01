import sys, functools

def solution(N, first, next, period):
    dp = [1]*(period + next)
    for i in range(next, period + next):
        dp[i] = dp[i - next] + dp[i - first]

    return sum(dp[period - n + next - 1] for n in N)

print(solution((int(n) for n in sys.stdin.read().split(',')), 9, 7, 256))
