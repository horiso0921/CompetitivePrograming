
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
def A():
    s = S()
    k = II()
    ans = 0
    lis = []
    i = 0
    tmp = 1
    while len(s) > i + 1:
        if s[i] == s[i + 1]:
            tmp += 1
        else:
            lis.append((s[i], tmp))
            tmp = 1
        i += 1
    lis.append((s[i], tmp))
    if lis[0][0] == lis[-1][0]:
        if len(lis) == 1:
            ans += k * lis[0][1] // 2
            print(ans)
            return
        ans -= (lis[0][1] // 2 + lis[-1][1] // 2) * (k - 1)
        ans += (lis[0][1] + lis[-1][1]) // 2 * (k - 1)
    for _, b in lis:
        ans += b // 2 * k
    print(ans)
    return
