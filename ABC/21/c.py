
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
def C():
    n = II()
    a, b = LI_()
    m = II()
    xy = LIR_(m)
    ans = [inf for i in range(n)]
    edg = [[] for i in range(n)]
    for x, y in xy:
        edg[x].append(y)
        edg[y].append(x)
    q = deque()
    q.append(a)
    ans[a] = 0
    while q:
        now = q.pop()
        for go in edg[now]:
            if ans[go] > ans[now] + 1:
                ans[go] = ans[now] + 1
                q.append(go)
    r = deque()
    r.append(b)
    dag = [[] for i in range(n)]
    bdag = [[] for i in range(n)]
    check = [True for i in range(n)]
    while r:
        now = r.pop()
        for go in edg[now]:
            if ans[go] + 1 == ans[now]:
                dag[go].append(now)
                bdag[go].append(now)
                if check[go]:
                    r.append(go)
                    check[go] = False
    def topolosort():
        cut = deque()
        while True:
            flg = True
            for d in bdag:
                for dd in d:
                    if len(bdag[dd]) == 0:
                        cut.appendleft(dd)
                        for d_ in bdag:
                            if dd in d_:
                                d_.remove(dd)
                                flg = False
            if flg:
                break
        cut.appendleft(a)
        return cut
    topdag = topolosort()
    dp = [0 for _ in range(n)]
    dp[a] = 1
    for da in topdag:
        for dad in dag[da]:
            dp[dad] += dp[da]
            dp[dad] %= mod
    print(dp[b])
    return

