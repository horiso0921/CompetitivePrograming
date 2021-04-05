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
    h, w = LI()
    a = SR(h)
    lis = defaultdict(list)
    for y in range(h):
        for x in range(w):
            if a[y][x] == "S":
                start = (y, x)
            if a[y][x] == "G":
                goal = (y, x)
            if a[y][x] != "#" and a[y][x] != ".":
                lis[a[y][x]].append((y, x))
    check = [[0] * 2000 for i in range(2000)]
    q = deque()
    q.append((start[0], start[1], 0))
    check[start[0]][start[1]] = True
    while q:
        y, x, s = q.popleft()
        c = lis[a[y][x]]
        for ci in c:
            if check[ci[0]][ci[1]]:
                continue
            check[ci[0]][ci[1]] = True
            q.append((ci[0], ci[1], s + 1))
        lis[a[y][x]] = []
        for my, mx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            my += y
            mx += x
            if 0 <= my < h and 0 <= mx < w:
                if a[my][mx] == "#": continue
                if check[my][mx]: continue
                check[my][mx] = True
                q.append((my, mx, s + 1))
                if (my, mx) == goal:
                    print(s + 1)
                    return
    print(-1)
    return


# main
if __name__ == '__main__':
    solve()