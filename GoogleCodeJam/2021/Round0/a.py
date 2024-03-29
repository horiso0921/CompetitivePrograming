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
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

# solve
def solve():
    t = II()
    for tt in range(t):
        n = II()
        l = LI()
        ans = 0
        for i in range(n - 1):
            tmp = inf
            x = 0
            for j in range(i, n):
                if tmp > l[j]:
                    x = j
                    tmp = l[j]
            if tmp == inf:
                break
            tmp = l[i: x + 1]
            tmp = tmp[::-1]
            l[i: x + 1] = tmp
            ans += x - i + 1
        print("Case #{}: {}".format(tt, ans))
    return


# main
if __name__ == '__main__':
    solve()