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
    n,k = LI()
    a = LI()
    ma = max(a)
    ans = 0
    for ai in a:
        ans += ma - ai
    if ans <= k:
        k -= ans
        k //= n
        print(ma + k)
    else:
        ans = 1
        cnt = [0] * (ma + 1)
        acc = [0] * (ma + 1)
        for ai in a:
            cnt[ai] += 1
            acc[ai] += ai
        cnt = list(itertools.accumulate(cnt))
        acc = list(itertools.accumulate(acc))
        for i in range(2, ma+1):
            tmp = 0
            for j in range(i, ma + 1, i):
                c = cnt[j] - cnt[j-i]
                s = acc[j] - acc[j-i]
                tmp += c*j - s
            c = cnt[-1] - cnt[j]
            s = acc[-1] - acc[j]
            tmp += c*(j+i) - s
            if tmp > k: continue
            ans = max(ans, i)
        print(ans)
            
    return


#main
if __name__ == '__main__':
    solve()