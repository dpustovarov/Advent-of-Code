import sys, numpy

def solution(N):
    return int(sum(numpy.absolute(N - numpy.median(N))))

print(solution([int(n) for n in sys.stdin.read().split(',')]))
