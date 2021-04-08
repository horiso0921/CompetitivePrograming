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
def SR(n): return ["."+S()+"." for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

# solve
def solve():
    h,w = LI()
    s = ["." * (w + 2)] + SR(h) + ["." * (w + 2)]
    ans = 0
    for hi in range(h):
        hi += 1
        for wi in range(w):
            wi += 1
            t = 0
            for mx, my in [(0,0),(1,0),(0,1),(1,1)]:
                mx += hi
                my += wi
                if s[mx][my] == "#": t ^= 1
            if t:
                ans += 1
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()