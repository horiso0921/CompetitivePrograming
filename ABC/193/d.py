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


def score(lis, i):
    lis[i] += 1
    res = 0
    for j in range(10):
        res += j * pow(10, lis[j])
    lis[i] -= 1
    return res


def solve():
    k = II()
    s = S()
    t = S()
    ans = 0
    tmp = [0] * 10
    tmps = [0] * 10
    tmpt = [0] * 10
    al = k * 9 - 8
    for si in s[:-1]:
        tmp[int(si)] += 1
        tmps[int(si)] += 1
    for ti in t[:-1]:
        tmp[int(ti)] += 1
        tmpt[int(ti)] += 1
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                tij = tmp[i]
                if tij + 2 > k:
                    continue
                scorei = score(tmps, i)
                scorej = score(tmpt, j)
                if scorei > scorej:
                    ij = k - tij
                    ans += ij * (ij - 1) / al / (al - 1)
            else:
                ti = tmp[i]
                tj = tmp[j]
                if ti + 1 > k or tj + 1 > k:
                    continue
                scorei = score(tmps, i)
                scorej = score(tmpt, j)
                if scorei > scorej:
                    ii = k - ti
                    jj = k - tj
                    ans += ii * jj / al / (al - 1)

    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
