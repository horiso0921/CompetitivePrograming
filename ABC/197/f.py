from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
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
    n, m = LI()
    abc = LSR(m)
    edg = [[] for _ in range(n)]
    for a, b, c in abc:
        a = int(a) - 1
        b = int(b) - 1
        edg[a].append((b, c))
        if a == b:
            continue
        edg[b].append((a, c))
    check = defaultdict(int)
    check[(0, n - 1)] = 1
    check[(n - 1, 0)] = 1
    q = deque()
    ans_ = inf
    q.append((0, n - 1, 0))
    while q:
        s, e, ans = q.popleft()
        tmp = defaultdict(list)
        for ei, c in edg[s]:
            tmp[c].append(ei)
        for si, c in edg[e]:
            if tmp[c]:
                for ti in tmp[c]:
                    if si == s and ti == e:
                        ans_ = min(ans_, ans + 1)
                        return
                    if si == ti:
                        ans_ = min(ans_, ans + 2)
                        return
                    if check[(si, ti)]:
                        continue
                    check[(si, ti)] = 1
                    check[(ti, si)] = 1
                    q.append((ti, si, ans + 2))
    if ans_ == inf:
        print(-1)
    else:
        print(ans_)
    return


# main
if __name__ == '__main__':
    solve()
