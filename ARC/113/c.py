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
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    s = S()[::-1]
    ans = 0
    ns = []
    dp = [0] * (ord("z") - ord("a") + 1)
    ns.append([s[0], 1])
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            ns[-1][-1] += 1
        else:
            ns.append([s[i], 1])
    tmp = 0
    for si, i in ns:
        if i >= 2:
            ans += tmp - dp[ord(si) - ord("a")]
            dp = [0] * (ord("z") - ord("a") + 1)
            tmp += i    
            dp[ord(si) - ord("a")] = tmp
        else:
            dp[ord(si) - ord("a")] += 1
            tmp += i    
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
