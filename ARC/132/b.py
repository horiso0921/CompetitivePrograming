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
    n = II()
    P = LI()
    
    if P == sorted(P):
        print(0)
        return
    
    if P[::-1] == sorted(P):
        print(1)
        return
    
    def f(p):
        ans = inf
        
        # 後ろに送り
        pre = p[0]
        if pre != 1:
            for i in range(1, n):
                if pre + 1 == p[i]:
                    pre += 1
                    continue
                if p[i] == 1:
                    ans = min(ans, i)
                else:
                    break
        # 後ろに送って最後反転
        pre = p[0]
        if pre != n:
            for i in range(1, n):
                if pre - 1 == p[i]:
                    pre -= 1
                    continue
                if p[i] == n:
                    ans = min(ans, 1+i)
                else:
                    break
        return ans
    
    print(min(f(P), 1 + f(P[::-1])))
    
        
            
    return


#main
if __name__ == '__main__':
    solve()