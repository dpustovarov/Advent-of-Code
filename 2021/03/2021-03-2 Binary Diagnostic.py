import sys

def solution(R):
    m, n = len(R), len(R[0])
    
    oxygen = {*R}
    for i in range(n):
        most = int(sum(r[i] for r in oxygen) >= len(oxygen)/2)
        oxygen = {r for r in oxygen if r[i] == most}
        if len(oxygen) == 1: break

    co2 = {*R}
    for i in range(n):
        least = int(sum(r[i] for r in co2) < len(co2)/2)
        co2 = {r for r in co2 if r[i] == least}
        if len(co2) == 1: break

    return sum(b << i for i, b in enumerate(reversed(oxygen.pop()))) * sum(b << i for i, b in enumerate(reversed(co2.pop())))
 
print(solution([tuple(map(int, s.strip())) for s in sys.stdin.readlines()]))