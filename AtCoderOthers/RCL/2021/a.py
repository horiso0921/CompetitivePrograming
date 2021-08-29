#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
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
mod = 1000000007
inf = 1e10

#solve
def solve():
    n,m,k = LI()
    a = LI()
    ans = []
    score = []
    tmp = 0
    for i in range(n):
        tmp += math.ceil(math.log2(k) - math.log2(a[i] + 1))
    score.append((tmp, 0))
    ma = [max(a), a.index(max(a))]
    for i in range(m):
        p = ma[1]
        q = ma[1]
        for j in range(n):
            if abs(a[j] + a[p] - k) < abs(a[q] + a[p] - k):
                q = j
        if a[p] == 0 or a[q] == 0: break
        tmp = score[-1][0] - math.ceil(math.log2(k) - math.log2(a[p] + 1))
        a[p] = (a[p] + a[q]) % k
        tmp += math.ceil(math.log2(k) - math.log2(a[p] + 1))
        score.append((tmp, i+1))
        ans.append((str(p), str(q)))
        ma = [max(a), a.index(max(a))]

    score.sort(reverse=True)
    for k in range(score[0][1]):
        print(*ans[k])
    return


#main
if __name__ == '__main__':
    solve()