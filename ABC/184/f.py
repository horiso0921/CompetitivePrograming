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
    n, t = LI()
    a = LI()
    ans1 = []
    ans = 0
    for mask in range(1 << (n >> 1)):
        tmp = 0
        for i in range(n >> 1):
            if mask & 1 << i:
                tmp += a[i]
        ans1.append(tmp)
    ans1.sort()
    for mask in range(1 << (n - (n >> 1))):
        tmp = 0
        for i in range((n - (n >> 1))):
            if mask & 1 << i:
                tmp += a[i + (n >> 1)]
        tt = t - tmp
        if tt < 0:
            continue
        an = ans1[bisect_right(ans1, tt) - 1]
        ans = max(ans, an + tmp)
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()