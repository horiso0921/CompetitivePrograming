
#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
def D():
    _, a, b = LI()
    v = LI()
    v.sort(reverse=True)
    d = defaultdict(int)
    ans = defaultdict(int)
    for vi in v:
        d[vi] += 1
    for i in range(a, b + 1):
        res = v[:i]
        r = res[-1]
        tmp = res.count(r)
        r = math.factorial(d[r]) / math.factorial(tmp) / math.factorial(d[r] - tmp)
        ans[sum(res) / i] += math.ceil(r-0.5)
    ans = list(ans.items())
    ans.sort(reverse=True, key = lambda x:x[0])
    print(ans[0][0])
    print(ans[0][1])
    return

