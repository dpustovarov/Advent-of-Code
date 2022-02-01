import sys, functools

def solution(N, first, next, period):

    @functools.cache
    def dp(p):
        return dp(p - next) + dp(p - first) if p >= next else 1

    return sum(dp(period - n + next - 1) for n in N)

print(solution((int(n) for n in sys.stdin.read().split(',')), 9, 7, 256))
