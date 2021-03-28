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


def smallest_prime_factors(n):
    spf = [i for i in range(n + 1)]
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf

def factolization(x, spf):
    ret = []
    while x != 1:
        ret.append(spf[x])
        x //= spf[x]
    ret.sort()
    return ret

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
    spf = smallest_prime_factors(m)
    ans = 0
    for j in range(1, m + 1):
        res = factolization(j, spf)
        tmp = 1
        for xi in res:
            x = 0
            while j % xi == 0:
                j //= xi
                x += 1
            tmp *= combination_mod(n + x - 1, x, mod)
            tmp %= mod
        ans += tmp
        ans %= mod
    print(ans)
    return


# main
if __name__ == '__main__':
    solve()
