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
    n = II()
    c = LI()
    edg = [[] for i in range(n)]
    for _ in range(n - 1):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    ans = [1]
    check = defaultdict(int)
    color = defaultdict(int)
    check[0] = 1
    color[c[0]] = 1
    def dfs(s):
        for e in edg[s]:
            if check[e]: continue
            check[e] = 1
            if color[c[e]] == 0:
                ans.append(e + 1)
            color[c[e]] += 1
            dfs(e)
            check[e] = 1
            color[c[e]] -= 1
    dfs(0)
    ans.sort()
    for ai in ans:
        print(ai)

    return


# main
if __name__ == '__main__':
    solve()