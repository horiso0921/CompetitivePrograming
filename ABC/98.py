#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b = LI()
    print(max(a + b, a - b, a * b))
    return

#B
def B():
    n = II()
    s = S()
    ans = 0
    for i in range(n + 1):
        s1 = list(set(s[i:]))
        s2 = list(set(s[:i]))
        b = 0
        for si in s1:
            b += si in s2
        ans = max(ans, b)
    print(ans)
    return

#C
def C():
    n = II()
    s = S()
    dp = [0 for i in range(n)]
    for num,si in enumerate(s):
        if si == "E":
            dp[num] = dp[num-1]+1
        else:
            dp[num] = dp[num - 1]
    ans = float("INF")
    a = max(dp)
    for i in range(n):
        ans = min(ans,  a - dp[i] + i - dp[i] + (s[i] == "E"))
    
    print(ans)
    return

#D
def D():
    n = II()
    a = LI()
    bitlength = len(bin(max(a))) - 2
    a = list(map(lambda x: bin(x)[:1:-1], a))
    cumulativebit = [[0] * bitlength for i in range(n)]
    for i in range(n):
        for bi in range(bitlength):
            cumulativebit[i][bi] += cumulativebit[i - 1][bi] + (0 if len(a[i]) <= bi else 1 if int(a[i][bi]) else 0)
    r = 0
    ans = 0
    for l in range(n):
        f = False
        cumulativebitl = cumulativebit[l]
        al = a[l]
        for r in range(r, n):
            cumulativebitr = cumulativebit[r]
            ar = a[r]
            for bi in range(bitlength):
                if cumulativebitr[bi] - cumulativebitl[bi] >= 2 or (l != r and len(ar) > bi and len(al) > bi and int(ar[bi]) and int(al[bi])):
                    f = True
                    break
            if f:
                break
        if f:
            ans += r - l
        else:
            ans += r - l + 1
    print(ans)
    return



#Solve
if __name__ == '__main__':
    D()
