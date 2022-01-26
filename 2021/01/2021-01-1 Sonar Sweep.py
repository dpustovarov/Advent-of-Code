import sys

def solution(R):
    return sum(a < b for a, b in zip(R, R[1:]))
 
print(solution([*map(int, sys.stdin.readlines())]))
