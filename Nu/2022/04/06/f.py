#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math, time
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
    stime = time.time()
    n,m,P = LI()
    abc = LIR(m)
    edg = [[] for _ in range(n)]
    redg = [[] for _ in range(n)]
    for a,b,c in abc:
        a -= 1
        b -= 1
        edg[a].append((b,c))
        redg[b].append(a)

    strong = [0] * n
    for i in range(n):
        check = [0] * n
        check[i] = 1
        q = [(0, i)]
        while q:
            coin, p = heappop(q)
            if time.time() - stime > 1.8:
                print(-1)
                return
            coin *= -1
            check[p] = 1
            for e, c in edg[p]:
                if e == i:
                    if P < coin + c:
                        strong[i] = 1
                        break
                elif check[e] != 1:
                    heappush(q, ( -(coin + c - P), e))
            if strong[i]:
                break
            
    can_move_to_n = [0] * n
    can_move_to_n[-1] = 1
    q = [n-1]
    for qi in q:
        for e in redg[qi]:
            if can_move_to_n[e]:
                continue
            q.append(e)
            can_move_to_n[e] = 1

    coin_l = [[-1] * (n) for _ in range(n+1)]
    coin_l[0][0] = 0
    for time_ in range(n):
        coin_lt = coin_l[time_]
        coin_lt1 = coin_l[time_+1]
        for i in range(n):
            coin = coin_lt[i]
            if coin >= 0:
                for e,c in edg[i]:
                    coin_lt1[e] = max(coin_lt1[e], coin + c)

    for i in range(n):
        if strong[i] and can_move_to_n[i]:
            for j in range(n+1):
                if coin_l[j][i] != -1:
                    print(-1)
                    return
    ans = 0
    for i in range(n+1):
        ans = max(ans, coin_l[i][n-1]-P*i)
    print(max(ans,0))

    return


#main
if __name__ == '__main__':
    solve()