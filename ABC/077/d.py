
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
# 俺は正数問題を解いていたと思ったらいつのまにかグラフ問題を解いていた
# 何を言ってるかわからねーと思うが自分もわからねぇ(ｒｙ)
# 変態
# 全部の数字は足す1もしくは×10で考えられて前者なら全体の和が1増えて後者なら
# 変わらないということに気づいたらいけるんだと思う（いけるとは言ってない）
# 倍数の下で何かをするというよりはそのKのmod下にて最小な桁和がいくつになるのか
# という考えに至るとほぼ勝ち
def D():
    k = II()
    dp = [inf] * k
    q = deque()
    q.append(1)
    dp[1] = 1
    while q:
        i = q.pop()
        if dp[(i * 10) % k] > dp[i]:
            dp[(i * 10) % k] = dp[i]
            q.appendleft((i * 10) % k)
        if dp[(i + 1) % k] > dp[i] + 1:
            dp[(i + 1) % k] = dp[i] + 1
            q.append((i + 1) % k)
    print(dp[0])
    return


