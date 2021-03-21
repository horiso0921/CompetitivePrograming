from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 1000000007
inf = 1e10
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

# solve
def solve():
    n = II()
    at = LIR(n)
    q = II()
    x = LI()
    ans = [None] * q
    for i in range(q):
        ans[i] = [x[i], i]
    ans.sort()
    l = -1
    lnum = -inf
    r = n
    rnum = inf
    res = 0
    for a, t in at:
        if t == 1:
            res += 1
        elif t == 2:
            ok = l
            ng = r
            while ng - ok > 1:
                mid = (ok + ng) // 2
                if ans[mid] + res >= a:
                    ng = mid
                else:
                    ok = mid
            lnum = a
            l = ok
        else:
            ok = r
            ng = l
            while ok - ng > 1:
                mid = (ok + ng) // 2
                if ans[mid] + res <= a:
                    ng = mid
                else:
                    ok = mid
            rnum = a
            r = ok
    prians = [None] * q
    for i in range(q):
        if i <= l:
            prians[ans[i][1]] = lnum
        
    return


# main
if __name__ == '__main__':
    solve()