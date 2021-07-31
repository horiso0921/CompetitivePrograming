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
mod = 1000000007
inf = 1e10



#solve
def solve():
    # 強連結成分分解(SCC): グラフGに対するSCCを行う
    # 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
    # 出力: (<ラベル数>, <各頂点のラベル番号>)
    def scc(N, G, RG):
        order = []
        used = [0]*N
        group = [None]*N
        def dfs(s):
            used[s] = 1
            for t in G[s]:
                if not used[t]:
                    dfs(t)
            order.append(s)
        def rdfs(s, col):
            group[s] = col
            used[s] = 1
            for t in RG[s]:
                if not used[t]:
                    rdfs(t, col)
        for i in range(N):
            if not used[i]:
                dfs(i)
        used = [0]*N
        label = 0
        for s in reversed(order):
            if not used[s]:
                rdfs(s, label)
                label += 1
        return label, group

    # 縮約後のグラフを構築
    def construct(N, G, label, group):
        G0 = [set() for i in range(label)]
        GP = [[] for i in range(label)]
        for v in range(N):
            lbs = group[v]
            for w in G[v]:
                lbt = group[w]
                if lbs == lbt:
                    continue
                G0[lbs].add(lbt)
            GP[lbs].append(v)
        return G0, GP
    
    N = II()
    s = SR(N)
    ds = defaultdict(list)
    de = defaultdict(list)
    for si in s:
        ds[si[:3]].append(si)
        de[si[-3:]].append(si)
    edg = [[] for i in range(N)]
    for k, v in de.items():
        for e in de[k]:
            for vi in 
    return


#main
if __name__ == '__main__':
    solve()