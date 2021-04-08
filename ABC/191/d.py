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
    x,y,r = LS()
    if "." in x:
        x = x.split(".")[0] + x.split(".")[1] + "0" * (4 - len(x.split(".")[1]))
    else:
        x = int(x) * 10000
    if "." in y:
        y = y.split(".")[0] + y.split(".")[1] + "0" * (4 - len(y.split(".")[1]))
    else:
        y = int(y) * 10000
    if "." in r:
        r = r.split(".")[0] + r.split(".")[1] + "0" * (4 - len(r.split(".")[1]))
    else:
        r = int(r) * 10000
    x = int(x)
    y = int(y)
    r = int(r)
    r2 = r ** 2
    ans = 0
    def ceil(x):
        return math.ceil(x/10000)
    def floor(x):
        return math.floor(x/10000)
    for xi in range(ceil(x-r)*10000, floor(x+r)*10000+1, 10000):
        def f(yi):
            tmp = (x - xi) ** 2 + (y - yi) ** 2
            return tmp <= r2
        ok = y
        ng = y + r + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if f(mid):
                ok = mid
            else:
                ng = mid
        a = ok
        ok = y
        ng = y - r - 1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if f(mid):
                ok = mid
            else:
                ng = mid
        b = ok
        a = floor(a)
        b = ceil(b)
        ans += a - b + 1
    print(ans)

    return


# main
if __name__ == '__main__':
    solve()
