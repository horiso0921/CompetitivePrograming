
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
# 2 <= b <= √n
# までに関しては全探索すればよくて
# ここで解がない場合はそれ以上を見る 
# √n < b <= n
# に関してはb進数表記で2桁になることが確定してて
# n = p*b+qとするなら p + q = s で(1 <= p < b, 0 <= q < b)
# n = p*b+q >= p*b > p**2 → √n > p がわかるからpを全探索
# b = (n-s)/p + 1なのでpを決めればbが決まってあとは調べればいい
# 数学じゃんこれ！ 
def D():
    def f(b, n):
        if n < b:
            return n
        return f(b, n // b) + (n % b)
    n, s = IR(2)
    if n == s:
        print(n + 1)
        return
    for b in range(2, int(math.sqrt(n)) + 1):
        if s == f(b, n):
            print(b)
            return
    for p in range(int(math.sqrt(n)), 0, -1):
        b = (n - s) // p + 1
        if b <= 1:
            continue
        if s == f(b, n):
            print(b)
            return
    print(-1)
    return


