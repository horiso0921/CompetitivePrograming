
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
# 解説AC
# a→bの辺に関していえばこの辺を2辺張ってしまえば2*n本で
# 2^n個のパスの組み合わせができることに気づけなかった
# i→i+1へ辺を出して長さは0 or 1<<i-1の辺を張ることで
# 和のi番目のbitを立たせるかを選ばせることができる
# さらに、Lのi番目のbitが立っているときにi番目のbitを立たせる
# もしくは最上位のbitを立たせてかつ、そのbitを除くi番目より上位の
# 立っているbitすべてを立たせたものの和を辺の長さとして辺を張ることで
# 解が得られる（はず）
def D():
    l = II()
    lBit = bin(l)[:1:-1]
    #print(lBit)
    n = len(lBit)
    ans = []
    for i in range(1, n):
        ans += [(i, i + 1, 0)] + [(i, i + 1, 1 << i - 1)]
    b = 1 << n - 1
    for i in range(n - 1):
        if lBit[-2 - i] == "1":
            ans += [(n - i - 1, n, b)]
            b += 1 << (n - i - 2)
    print(n,len(ans))
    for a in ans:
        print(*a)
    return


