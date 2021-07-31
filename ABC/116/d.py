
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
# 大きいものからとっていった際にその種類数をn
# としてi<=nの種類数においてこれを超えるものは無い
# それより大きいものについて種類数が減らずかつとったものの中で
# 一番小さいものを除き、種類数が増える一番大きいものをとってこれば
# i+1番目の種類下でもっとも大きい数になる 
def D():
    n, k = LI()
    ma = []
    for _ in range(n):
        t, di = LI()
        ma.append((di, t))
    ma.sort()
    ma = deque(ma)
    s = defaultdict(int)
    t = 0
    ans = 0
    q = []
    for _ in range(k):
        di,ti = ma.pop()
        ans += di
        heappush(q, (di, ti))
        if not s[ti]:
            t += 1
        s[ti] += 1
    ans += t ** 2
    ans = [ans]
    while ma and q:
        di, ti = ma.pop()
        while s[ti] and ma:
            di, ti = ma.pop()
        if not ma and s[ti]:
            break
        d1, t1 = heappop(q)
        while s[t1] == 1 and q:
            d1, t1 = heappop(q)
        if not q and s[t1] == 1:
            break
        s[t1] -= 1
        tmp = ans[-1]
        tmp = tmp - d1 + di - t ** 2
        t += 1
        tmp += t ** 2
        ans.append(tmp)
        heappush(q, (di, ti))
        s[ti] += 1
    print(max(ans))


    return

