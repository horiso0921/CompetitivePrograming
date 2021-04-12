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
    for _ in range(t):
        n, k = LI()
        if k > (n - 1) // 2:
            print(-1)
            continue
        if n == 1:
            print(1)
            continue
        if n == 2:
            print(1, 2)
            continue
        if k == 0:
            print(*range(1, n + 1))
            continue
        ans = [1, 3, 2]
        pre = 2
        for _ in range(k - 1):
            ans.append(pre + 3)
            ans.append(pre + 2)
            pre += 2
        for i in range(pre + 2, n + 1):
            ans.append(i)
        print(*ans)
        continue
    return


# main
if __name__ == '__main__':
    solve()