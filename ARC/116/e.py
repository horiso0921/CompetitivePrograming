from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 1000000007
inf = 1e10
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

# solve
def solve():
    n, k = LI()
    edg = [[] for i in range(n)]
    for _ in range(n - 1):
        u, v = LI_()
        edg[u].append(v)
        edg[v].append(u)

    c = [False] * n
    ma = 0
    map_ = None
    q = deque()
    q.append((0, 0))
    while q:
        p, s = q.popleft()
        if c[p]:
            continue
        c[p] = True
        for e in edg[p]:
            if c[e]: continue
            q.append((e, s + 1))
            if ma < s + 1:
                ma = s + 1
                map_ = e
    start = map_
    
    c = [False] * n
    ma = 0
    map_ = None
    q = deque()
    q.append((start, 0))
    while q:
        p, s = q.popleft()
        if c[p]:
            continue
        c[p] = True
        for e in edg[p]:
            if c[e]: continue
            q.append((e, s + 1))
            if ma < s + 1:
                ma = s + 1
                map_ = e
    
    ok = n
    ng = 0
    def f(mid):

        return 
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return


# main
if __name__ == '__main__':
    solve()