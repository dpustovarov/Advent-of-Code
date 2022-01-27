import sys

def solution(R):
    m, n = len(R), len(R[0])
    gamma = sum(1 << n-i for i, col in enumerate(zip(*R), 1) if sum(col) > m//2)
    epsilon = (1 << n) + ~gamma

    return gamma * epsilon
 
print(solution([tuple(map(int, s.strip())) for s in sys.stdin.readlines()]))
