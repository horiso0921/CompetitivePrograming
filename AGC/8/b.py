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
    n, k = LI()
    a = LI()
    ans = 0
    for ai in a:
        if ai > 0:
            ans += ai
    tmp = 0
    tmp2 = 0
    ans_t = 0
    for i in range(k):
        tmp += a[i]
        if a[i] > 0:
            tmp2 += a[i]
    for i in range(n - k):
        if tmp > 0:
            ans_t = max(ans_t, ans - tmp2 + tmp)
        else:
            ans_t = max(ans_t, ans - tmp2)
        tmp -= a[i]
        tmp += a[i + k]
        if a[i] > 0:
            tmp2 -= a[i]
        if a[i + k] > 0:
            tmp2 += a[i + k]
    if tmp > 0:
        ans_t = max(ans_t, ans - tmp2 + tmp)
    else:
        ans_t = max(ans_t, ans - tmp2)
    print(ans_t)
    return


# main
if __name__ == '__main__':
    solve()