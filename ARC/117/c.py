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
    def lu(n, k):
        res = 1
        while n and k:
            n3 = n % 3
            k3 = k % 3
            if n3 < k3:
                return 0
            if n3 == 0 or k3 == 0:
                pass
            else:
                if n3 == k3:
                    pass
                else:
                    res *= n3
            n //= 3
            k //= 3
        return res
    n = II()
    c = S()
    d = {"B": 0, "W": 1, "R": 2}
    l = ["B", "W", "R"]
    ans = 0
    for i in range(n):
        ans += d[c[i]] * lu(n - 1, i)
        ans %= 3
    print(l[[-1,1][n&1]*ans%3])

    return


# main
if __name__ == '__main__':
    solve()