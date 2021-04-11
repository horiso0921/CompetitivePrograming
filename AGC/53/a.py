from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
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
    s = S()
    v = LI()
    def f(i):
        ans = [[k // i + (k % i > j) for k in v] for j in range(i)]
        # if i % 10**2 == 0: print(ans[0])
        for j in ans:
            for k in range(n):
                if s[k] == "<" and j[k] >= j[k + 1]:
                    return False
                if s[k] == ">" and j[k] <= j[k + 1]:
                    return False
        return True
    
    ok = 1
    ng = 10 ** 4 + 1
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    i = ok
    ans = [[k // i + (k % i > j) for k in v] for j in range(i)]
    print(ok)
    for ai in ans:
        print(*ai)
    return


# main
if __name__ == '__main__':
    solve()
