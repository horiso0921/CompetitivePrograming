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
    for I in range(II()):
        I += 1
        print(f"Case #{I}: ", end="")
        s = S()[::-1]
        ans = [s[0]]
        pre = s[0]
        f = 0
        for si in s[1:]:
            if si < pre:
                ans.append(si)
                ans.append(si)
            else:
                if si == pre:
                    if f: # 前回のUniqが自分より大きい奴
                        ans.append(si)
                        ans.append(si)
                    else:
                        ans.append(si)
                else:
                    ans.append(si)
            
            if si < pre:
                f = 1
            
            if pre < si:
                f = 0
            
            pre = si
        print("".join(ans[::-1]))

    return


#main
if __name__ == '__main__':
    solve()