
#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#solve
# 解説AC
# ある点kにおいて2つに分けてa'の
# 前後半の要素を考える
# シンプルにわからなかった 
def D():
    n = II()
    a = LI()
    first_half_list = []
    final_half_list = []
    first_half_sum = deque([0])
    final_half_sum = deque([0])
    ans = -inf
    for i in range(n):
        heappush(first_half_list, a[i])
        first_half_sum[0] += a[i]
        heappush(final_half_list, -a[-i - 1])
        final_half_sum[0] -= a[-i - 1]
    for i in range(1, n + 1):
        q = heappop(first_half_list)
        heappush(first_half_list, max(q, a[i + n - 1]))
        first_half_sum.append(first_half_sum[-1] - q + max(q, a[i + n- 1]))
        q = heappop(final_half_list)
        heappush(final_half_list, max(q, -a[-n - i]))
        final_half_sum.appendleft(final_half_sum[0] - q + max(q, -a[-n - i]))
    for i in range(n + 1):
        ans = max(ans, first_half_sum[i] + final_half_sum[i])
    print(ans)
    return


