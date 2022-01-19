import sys, itertools

def solution(R):
    A, B = itertools.tee(R)
    next(B)
    return sum(a < b for a, b in zip(A, B))
 
print(solution(map(int, sys.stdin.readlines())))
