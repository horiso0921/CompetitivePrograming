#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b, c, d = LI()
    if b / a < d / c:
        print("AOKI")
    elif b / a > d / c:
        print("TAKAHASHI")
    else:
        print("DRAW")
    return

#B
def B():
    n, m = LI()
    a = (n%12) * 30 + 0.5 * m
    b = m * 6
    print(min(abs(a - b), abs(360 - a + b), abs(360 - b + a)))
    return

#C
def C():
    LI()
    x, y = LI()
    a = LI()+[inf]
    b = LI()+[inf]
    ai, bi, now, tern = [0] * 4
    ans = 0
    while 1:
        if tern:
            if b[bi] == inf:
                break
            if b[bi] >= now:
                now = b[bi] + y
                bi += 1
                ans += 1
                tern ^= 1
            else:
                bi += 1
        else:
            if a[ai] == inf:
                break
            if a[ai] >= now:
                now = a[ai] + x
                ai += 1
                tern ^= 1
            else:
                ai += 1
    print(ans)

    return

# D
# 解説AC
# k <= nなら制約からシミュレーションすればいいことがわかる
# k > nのとき閉路が発生してかつ閉路の中で状態が終了する
# 1 → 2 → 3 → 4 → 5 → 6
#         ↑           ↓
#         ↑ ← 9 ← 8 ← 7
# 閉路サイズ7 スタート1
# k=10とするなら10%7=3
# 閉路に入るまでの距離が2なので
# 1からシミュレーションする
# k=15とするなら15%7=1
# 閉路に入るまでの距離より小さいので
# Cを足して8としてこれをシミュレーションする
# というのが解説 
# ------------------------------------------------------
# この解法ではわかりづらいので自分が考えたのは下のとおり
# 上の例でk=10として閉路までの距離は2なので(k-2)%7
# として考えるとわかりやすくこの時は閉路のスタート位置から始める
# 従来のスタートから始めるなら(k-2)%7+2となる
# k=15では(15-2)%7=6が閉路のスタート位置からの距離でそうでないときは
# (15-2)%7+2=8
# -------------------------------------------------------
# 以下は解説の理解(自分なり)
# 1 → 2 → 3 → 4 → 5 → 6
#                 ↑   ↓
#                 ↑ ← ←
# k=11とするなら閉路のサイズ2
# (11-4)%2+4=5 ここで 11%2=1これは閉路までの距離4より小さく
# スタートからのシミュレーションでは閉路に到達しない
# 閉路に到達するまでの距離を足してもよいが、閉路までの距離より大きくなるまで
# 閉路のサイズを足す
# この時の値をlとすると以降l+閉路のサイズをしても位置が変わらないことがわかる
# 更に閉路のサイズを足し続けるとl=kになることもわかる
# 以上より閉路のサイズを足してスタートまでの距離より大きくすることは
# 妥当なものであると言える 
def D():
    n, a = LI()
    k = II()
    b = LI()
    if k <= n:
        for _ in range(k):
            a = b[a - 1]
        print(a)
        return
    closed_circle = defaultdict(int)
    l = 1
    n = a
    while 1:
        if closed_circle[n]:
            a = n
            l = l - closed_circle[n]
            t = closed_circle[n] - 1
            break
        closed_circle[n] = l
        n = b[n-1]
        l = l + 1
        continue
    ans = (k - t) % l
    for _ in range(ans):
        a = b[a - 1]
    print(a)
    return


#Solve
if __name__ == '__main__':
    D()
