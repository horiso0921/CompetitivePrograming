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
    a = LI()
    ans = 0
    for ai in a:
        ans |= ai
    for mask in range(1 << n):
        full = []
        for i in range(n - 1):
            if (mask >> i & 1) ^ (mask >> (i + 1) & 1):
                full.append(i + 1)
        # print(full, (mask & (1 << 0)), (mask & (1 << 1)), (mask & (1 << 2)))
        f = [0] + list(full) + [n]
        tmpl = []
        for i in range(len(f) - 1):
            tmp = 0
            for j in range(f[i], f[i + 1]):
                tmp |= a[j]
            tmpl.append(tmp)
        tmp = 0
        for ti in tmpl:
            tmp ^= ti
        ans = min(ans, tmp)
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
