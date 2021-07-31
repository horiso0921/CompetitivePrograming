
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
def E():
    start = time.time()
    n = II()
    a = LIR_(n)
    ans = 0
    tern = [0] * n
    while 1:
        ans += 1
        f = True
        c = defaultdict(int)
        for i in range(n):
            if c[i]:
                continue
            if tern[i] == n - 1:
                continue
            rival = a[i][tern[i]]
            if c[rival]:
                continue
            if tern[rival] == n - 1:
                continue
            if a[rival][tern[rival]] == i:
                c[i] += 1
                c[rival] += 1
                tern[rival] += 1
                tern[i] += 1
                f = False
        if time.time() - start >= 1:
            print(n * (n - 1) // 2)
            return
        if f:
            if tern == [n - 1] * n:
                print(ans-1)
                return
            else:
                print(-1)
                return
    return

