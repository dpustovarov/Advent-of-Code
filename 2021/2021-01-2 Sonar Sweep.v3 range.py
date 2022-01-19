import sys

def solution(R):
    return sum(R[i] < R[i+3] for i in range(len(R)-3))
 
print(solution([*map(int, sys.stdin.readlines())]))
