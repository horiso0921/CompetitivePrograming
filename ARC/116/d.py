from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
mod = 998244353
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


fact = [i for i in range(4 * 10 ** 5 + 1)]
fact[0] = 1
for i in range(4 * 10 ** 5):
    fact[i + 1] *= fact[i]
    fact[i + 1] %= mod

invfact = fact[::]

invfact[-1] = pow(invfact[-1], mod - 2, mod)

for j in range(4 * 10 ** 5, 0, -1):
    invfact[j - 1] = invfact[j] * j
    invfact[j - 1] %= mod


def combination_mod(n, k, mod):
    """ power_funcを用いて(nCk) mod p を求める """
    """ nCk = n!/((n-k)!k!)を使用 """
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    a = fact[n] % mod
    return (a * invfact[k] * invfact[n-k] % mod)

# solve
def solve():
    n, m = LI()
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(20):
        b = 1 << i
        ndp = [0] * (m + 1)
        for x in range(m + 1):
            if dp[x] == 0: continue
            tmp = 0
            for j in range(0, n + 1, 2):
                if x + tmp > m:
                    break
                ndp[x + tmp] += dp[x] * combination_mod(n, j, mod)
                ndp[x + tmp] %= mod
                tmp += b * 2
        dp = ndp

    print(dp[-1])
    return


# main
if __name__ == '__main__':
    solve()
