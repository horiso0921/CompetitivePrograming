#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
    s = S()
    k = II()
    d = defaultdict(list)
    ans = defaultdict(int)
    for i in range(len(s)):
        d[s[i]].append(i)
    ans[(0,0,0,0)] = 1
    tra = {0:"K", 1:"E", 2:"Y"}
    for i in range(len(s)):
        nans = defaultdict(int)
        for key, val in ans.items():
            for x in range(3):
                nkey = list(key)
                nkey[x] += 1
                tkey = tra[x]
                if len(d[tkey]) < nkey[x]:
                    continue
                nkeyi = d[tkey][nkey[x]-1]
                tmp = 0
                for j in range(3):
                    if x != j:
                        for xx in d[tra[j]][:key[j]]:
                            if xx >= nkeyi:
                                tmp += 1
                tmp = max(0, nkeyi + tmp - i)
                nkey[3] += tmp
                nans[tuple(nkey)] += val
        ans = nans
    num = 0
    for key, val in ans.items():
        if key[-1] <= k:
            num += val
    print(num)
                
                
                
    return


#main
if __name__ == '__main__':
    solve()