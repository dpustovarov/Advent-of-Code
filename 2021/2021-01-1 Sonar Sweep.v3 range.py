import sys

def solution(R):
    return sum(R[i] < R[i+1] for i in range(len(R)-1))
 
print(solution([*map(int, sys.stdin.readlines())]))
