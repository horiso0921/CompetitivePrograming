#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**8)
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
def solve(n):

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

    lp = [0] * n
    edg = [[] for i in range(n)]
    redg = [[] for i in range(n)]
    for i in range(n):
        p,_,*a = LS()
        p = float(p)
        lp[i] = p
        a = list(map(lambda x:int(x) - 1, a))
        edg[i] = sorted(a)
        for ai in a:
            redg[ai].append(i)

    # label := <ラベル数>
    # group := <各頂点のラベル番号>
    label, group = scc(n, edg, redg)

    # G0 := [<各ラベルから生えている辺の相手ラベルのset>]
    # GP := [<各頂点のラベル番号>]
    G0, GP = construct(n, edg, label, group)

    # Gprob_tmp := [<各ラベルの要素ごとの寝坊確率>]
    # Gprob     := [<各ラベルの寝坊確率>]
    Gprob_tmp = [[lp[x] for x in GP[l]] for l in range(label)]
    Gprob = [0 for _ in range(label)]

    # 各ラべルの寝坊確率を求める
    for i in range(label):
        tmp = 1
        for xi in Gprob_tmp[i]:
            tmp *= xi
        Gprob[i] = tmp

    # 各ラべルに入ってくる辺があるかどうか
    # 辺が無ければDAGの先頭
    rG0 = [0] * (label)
    ans = 1

    # 逆辺を貼る
    for i in range(label):
        for e in G0[i]:
            rG0[e] |= 1

    # 逆辺が無ければDAGの先頭
    for i in range(label):
        if rG0[i]: continue
        ans *= 1 - Gprob[i]

    print(f"{ans:06f}")
    return


#main
if __name__ == '__main__':
    while 1:
        n = II()
        if n == 0: break    
        solve(n)