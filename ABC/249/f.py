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
inf = float("INF")

#solve
def solve():
    n, k = LI()
    ty = LIR(n)
    ans = -inf
    tmp = 0
    llis = []
    for t,y in ty[::-1] + [(1, 0)]:
        if t == 1:
            ans = max(ans, tmp + y)
            if len(llis) == k and k != 0:
                tmp -= heappop(llis)
            k -= 1
            if k < 0:
                break
        else:
            if y >= 0:
                tmp += y
            else:
                if len(llis) < k:
                    heappush(llis, -y)
                else:
                    if llis:
                        l = -heappop(llis)
                        if l > y:
                            heappush(llis, -y)
                            tmp += l
                        else:
                            heappush(llis, -l)
                            tmp += y
                    else:
                        tmp += y
                        # print(tmp)
    print(ans) 
                
            
    return


#main
if __name__ == '__main__':
    solve()