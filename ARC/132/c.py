#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
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
mod = 998244353
inf = float("INF")

#solve
def solve():
    n,D = LI()
    a = LI_()
    q = [1] * n
    qq = []
    qqq = []
    for i in range(n):
        if a[i] != -2:
            q[a[i]] = 0
        else:
            qq.append(i)
    if 1 not in q:
        print(1)
        return

    k = [inf] * (D + 1)
    q0 = qq[0]
    j = 0
    for i in range(n):
        if q[i]:
            qqq.append(i)
            if abs(i - q0) <= D:
                k[j] = i
                j += 1

    d = defaultdict(int)
    for i in range(len(k)):
        if k[i] == inf:
            continue
        nk = k[::1]
        nk[i] = inf
        d[tuple(sorted(nk))] = 1

    for qi in qq[1:]:
        nd = defaultdict(int)
        nex = []
        while j < len(qqq):
            if abs(qqq[j] - qi) <= D:
                nex.append(qqq[j])
                j += 1
            else:
                break
        for k,v in d.items():
            k = list(k)
            x = 0
            for ki in range(len(k)):
                if k[ki] == inf:
                    if len(nex) <= x: continue
                    k[ki] = nex[x]
                    x += 1
                elif abs(k[ki] - qi) > D:
                    break
            else:
                for ki in range(len(k)):
                    if k[ki] != inf:
                        nk = k[::1]
                        nk[ki] = inf
                        nk = tuple(sorted(nk))
                        nd[nk] += v
                        nd[nk] %= mod
        d = nd
    print(sum(d.values()) % mod)
                        
    
    
    return


#main
if __name__ == '__main__':
    solve()