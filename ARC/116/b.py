from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 998244353
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
    a = LI()
    a.sort()
    d = defaultdict(int)
    for ai in a:
        d[ai] += 1
    ans = 0
    tmp = 0
    tmp2 = 0
    for k, v in sorted(d.items()):
        tmp1 = tmp * ((1 << v) - 1) + ((1 << v) - 1) * k
        tmp1 %= mod
        ans += tmp1 * k
        tmp += tmp1
        tmp %= mod
        ans %= mod
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
