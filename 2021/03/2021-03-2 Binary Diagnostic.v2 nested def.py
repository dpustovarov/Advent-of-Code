import sys, operator

def solution(R):
    m, n = len(R), len(R[0])

    def rating(op):
        selected = {*R}
        for i in range(n):
            criteria = int(op(sum(s[i] for s in selected), len(selected)/2))
            selected = {s for s in selected if s[i] == criteria}
            if len(selected) == 1: break

        return sum(b << i for i, b in enumerate(reversed(selected.pop())))

    return rating(operator.ge) * rating(operator.lt)
 
print(solution([tuple(map(int, s.strip())) for s in sys.stdin.readlines()]))