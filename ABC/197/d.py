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
    x0, y0 = LF()
    x2, y2 = LF()
    dist = sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)
    a = dist * math.sin(math.pi / n) / math.sin(math.pi / 2)
    x = x2 - x0
    y = y2 - y0
    s = - (n - 2) / n / 2 * math.pi
    ans = [x0 + a / dist * (x * math.cos(s) - y * math.sin(s)),
           y0 + a / dist * (y * math.cos(s) + x * math.sin(s))]
    print(ans[0] , ans[1] )
    return


# main
if __name__ == '__main__':
    solve()
