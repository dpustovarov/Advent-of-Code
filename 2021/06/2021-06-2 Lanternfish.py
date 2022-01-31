import sys, collections, math

def solution(N, first, next, period):
    return sum(c*sum(math.comb(-((period - n - i*first)//-next) + i, i+1) for i in range(-1, -((period - n)//-first))) for n, c in collections.Counter(N).items()) 

print(solution((int(n) for n in sys.stdin.read().split(',')), 9, 7, 256))
