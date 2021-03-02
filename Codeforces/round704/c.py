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
    n,m = LI()
    s = S()
    t = S()
    dp1 = []
    dp2 = []
    j = 0
    for i in range(n):
        if t[j] == s[i]:
            j += 1
            dp1.append(i)
        if j == m:
            break
    s = s[::-1]
    t = t[::-1]
    j = 0
    for i in range(n):
        if t[j] == s[i]:
            j += 1
            dp2.append(n-i-1)
        if j == m:
            break
    dp2 = dp2[::-1]
    ans = 1
    for i in range(m-1):
        ans = max(ans, dp2[i+1]-dp1[i])
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
