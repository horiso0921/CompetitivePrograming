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
inf = float("INF")

#solve
def solve():
    n, k = LI()
    s = S()
    ans = []
    d_t = defaultdict(int)
    d_p = defaultdict(int)
    for si in s:
        d_p[si] += 1
        d_t[si] += 1
    tmp = 0
    for i in range(n - 1):
        si = s[i + 1 :]
        for key, value in sorted(d_t.items()):
            if value == 0:
                continue
            d_t[key] -= 1
            d_p[s[i]] -= 1
            if key == s[i]:
                ans.append(key)
                break
            else:
                buf = n - i
                for k_, v in d_t.items():
                    buf -= min(v, d_p[k_])
                if buf + tmp > k:
                    d_t[key] += 1
                    d_p[s[i]] += 1
                else:
                    tmp += 1
                    ans.append(key)
                    break
    for key, value in d_t.items():
        if value:
            ans.append(key)
    print("".join(ans))


    return


#main
if __name__ == '__main__':
    solve()
