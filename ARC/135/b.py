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
    n = II()
    s = LI()
    def f(start):
        s1 = 0
        ans = [0, inf]
        for i in range(start, n-1, 3):
            s1 += s[i] - s[i+1]
            ans[0] = max(ans[0], s1)
            ans[1] = min(ans[1], s1)
        return ans
    ans1 = f(0)[0]
    ans2 = f(1)[0]
    ans3 = f(2)[0]
    # return
    if ans1 + ans2 + ans3 > s[0]:
        print("No")
    else:
        print("Yes")
        ans = [0, ans1, ans2]
        ss = sum(ans)
        for i in range(n):
            ss -= ans[i]
            a = s[i] - ss
            ans.append(a)
            ss += a
        print(*ans[1:])
            
    
        
    return


#main
if __name__ == '__main__':
    solve()