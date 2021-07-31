
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
# √nまでで約数の全列挙ができるということは
# n <= a * b (a <= bとしたときに)
# 各 a は √nまでしかないことはわかる
# ( a > √n なら b < √n だからね)
# すると各aに対して対応するbの最大値が存在するため
# b の個数は高々 √n 個しか無いことがわかる
# 後はDPでどうぞ 
def F():
    n, k = LI()
    f = defaultdict(int)
    Range = int(sqrt(n))
    dp = [0] * (2 * Range)
    m = 0
    l = 0
    for i in range(Range, 0, -1):
        dp[i - 1] = 1
        f[i - 1] = 1
        if n // i == i:
            l = 1
            continue
        dp[Range + m] = n // i - n // (i + 1)
        f[Range + m] = n // i - n // (i + 1)
        m += 1
    R = 2 * Range - l
    for _ in range(k - 1):
        ndp = [0] * (2 * Range)
        for j in range(R):
            ndp[R - j - 1] = dp[j]
        ndp = list(itertools.accumulate(ndp[::-1]))[::-1]
        dp = [(d * f[num]) % mod for num,d in enumerate(ndp)]
    ans = sum(dp)%mod
    print(ans)
    return



