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
    r1, c1 = LI()
    r2, c2 = LI()
    ans = 10
    for r in range(-3, 4):
        for c in range(-3, 4):
            tmp = 1
            if r == c == 0:
                tmp -= 1
            tr = r1+r
            tc = c1+c
            if tr == r2 and tc == c2:
                ans = min(ans, tmp)
                continue
            rc2 = r2 + c2
            rc1 = tr + tc
            if abs(rc2-rc1) & 1:
                continue
            x = rc2-rc1
            x //= 2
            tr += x
            tc += x
            if tr == r2 and tc == c2:
                tmp += 1
            else:
                if x == 0:
                    tmp += 1
                else:
                    tmp += 2
            ans = min(ans, tmp)
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
