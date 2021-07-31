
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
def D():
    n, K = LI()
    s = S()
    ans = []
    i = 0
    while i < n:
        l = 1
        for x in range(i+1, n):
            if s[x] == s[i]:
                l = x + 1 - i
                continue
            l = x - i
            break
        ans.append(l)
        i += l
    f = 0
    if s[-1] == "0":
        ans.append(0)
        f = 1
    
    dp = [0 for i in range(len(ans))]
    #print(ans)    
    if s[0] == "0":
        i = 2*K
        dp[0] = sum(ans[:i])
        a = 1
    if s[0] == "1":
        i = 2*K+1
        dp[0] = sum(ans[:i])
        a = 0
    x = 1
    while x + 2 * K < len(ans):
        if not a:
            dp[x] = dp[x - 1] - ans[x-1]
        else:
            dp[x] = dp[x - 1] + ans[x + 2 * K] + ans[x+2*K-1] - ans[x-1]
        x += 1
        a = (a + 1) % 2
        
    print(max(dp))
        

    return

