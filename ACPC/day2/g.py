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
inf = 1e10

#solve
def solve():
    N, U = LI()
    U -= 1
    edg = [[] for i in range(N)]
    for _ in range(N-1):
        a,b = LI_()
        edg[a].append(b)    
        edg[b].append(a)    
        
    size = [1] * N
    rank = [inf] * N
    rank[U] = 0
    q = [U]
    for qi in q:
        for e in edg[qi]:
            if rank[e] > rank[qi]:
                rank[e] = rank[qi] + 1
                q.append(e)
    
    que = [[] for i in range(N)]

    for i in range(N):
        que[rank[i]].append(i)
    
    # 二次元配列作成
    dv = []
    for _ in range(int(math.log2(N)) + 1):
        l = [0] * N
        dv.append(l)

    for i in range(N - 1, -1, -1):
        for e in que[i]:
            for ne in edg[e]:
                if rank[e] > rank[ne]:
                    size[ne] += size[e]
                    # dv[0][0:N]を初期化
                    dv[0][e] = ne
    
    # ダブリングで表を構築
    for k in range(1, int(math.log2(N)) + 1):
        dvk = dv[k]
        dvk1 = dv[k-1]
        for n in range(N):
            dvk[n] = dvk1[dvk1[n]]
    
    ans = 0

    for i in range(N):
        if i == U: continue
        s = rank[i]
        s = s // 2
        e = i
        j = 0
        while s >= (1<<j):
            if s & (1<<j):
                e = dv[j][e]
            j += 1
        ans += N - size[e]
        ans %= mod
    print((ans * pow(N-1, mod-2, mod)) % mod)
    return


#main
if __name__ == '__main__':
    solve()