from itertools import accumulate
from collections import defaultdict
def f(n, m):
    h = [0]+[int(input()) for i in range(n)]
    w = [0]+[int(input()) for i in range(m)]
    res = 0
    acch = list(accumulate(h))
    accw = list(accumulate(w))
    lh = defaultdict(int)
    lw = defaultdict(int)
    for i in range(n+1):
        for j in range(i + 1, n+1):
            lh[acch[j]-acch[i]] += 1 
    for i in range(m+1):
        for j in range(i + 1, m+1):
            lw[accw[j] - accw[i]] += 1
    for key, val in lh.items():
        res += val * lw[key]
    return res

n, m = map(int, input().split())
while n != 0 and m != 0:
    print(f(n,m))
    n, m = map(int, input().split())
