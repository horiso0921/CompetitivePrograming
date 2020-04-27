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
    s = S()
    n = II()
    l = list(itertools.product(s, repeat=2))
    print("".join(l[n-1]))
    return

#B
def B():
    n, a, b = LI()
    ans = 0
    for _ in range(n):
        s, d = LS()
        d = int("".join(d))
        d = a * (d < a) or b * (d > b) or d
        ans += d * [1, -1][s[0] == "W"]
    print("East " * (ans > 0) + "West " * (ans < 0)+str(abs(ans)))
    return

#C
def C():
    b = LIR(2)
    c = LIR(3)

    def clc_score(field):
        ansb1 = 0
        ansb2 = 0
        for i,bi in enumerate(b):
            for j, bij in enumerate(bi):
                if field[i][j] == field[i + 1][j]:
                    ansb1 += bij
                else:
                    ansb2 += bij
        for i, ci in enumerate(c):
            for j, cij in enumerate(ci):
                if field[i][j] == field[i][j + 1]:
                    ansb1 += cij
                else:
                    ansb2 += cij
        return ansb1 - ansb2

    cross = itertools.combinations(range(9), 4)
    d = defaultdict(int)
    score = 0

    for bi in b:
        score += sum(bi)
    for ci in c:
        score += sum(ci)

    for cr in cross:
        field = [[0] * 3 for _ in range(3)]
        for ci in cr:
            field[ci // 3][ci % 3] = 1
        d[cr] = clc_score(field)


    def game_dfs(check, tern, cross):

        if tern == 10:
            cross.sort()
            return d[tuple(cross)]

        if tern % 2:
            res = -inf
            for i in range(9):
                if check[i]:
                    check[i] = False
                    res = max(game_dfs(check, tern + 1, cross), res)
                    check[i] = True
            return res

        else:
            res = inf
            for i in range(9):
                if check[i]:
                    check[i] = False
                    res = min(game_dfs(check, tern + 1, cross+[i]), res)
                    check[i] = True
            return res

    x = game_dfs([True] * 9, 1, [])
    print((score + x) // 2)
    print((score - x) // 2)

    return

#D
def D():
    def f(i, j):
        """ 
        i : その文字を入れることができる場所bit 
        j : いま文字が入っている場所をを表す数字 
        """
        u = Bit[i - 5] if i > 4 else False
        d = Bit[i + 5] if i < 20 else False
        l = Bit[i - 1] if i % 5 else False
        r = Bit[i + 1] if (i + 1) % 5 else False
        if u and d and ((u & j and not (d & j)) or (d & j and not (u & j))):
            return False
        if l and r and ((l & j and not (r & j)) or (r & j and not (l & j))):
            return False
        return True

    Field = LIR(5)
    Bit = [1 << i for i in range(25)]
    Used_num = [0] * 26
    Vacant_space = [i for i in range(25)]
    for y in range(5):
        for x in range(5):
            if Field[y][x]:
                yx = y * 5 + x
                Used_num[Field[y][x]] = yx + 1 # +1することで(0,0)が埋まっているときも対応する
                Vacant_space.remove(yx)

    pd = defaultdict(int)
    pd[0] = 1

    for i in range(1, 26):
        # 数字iがすでに盤面に書かれている場合はその場所を
        # そうでない場合は0が書かれている場所を返す
        if Used_num[i]:
            Vs = [Used_num[i] - 1]
        else:
            Vs = Vacant_space

        nd = defaultdict(int)   # 次の盤面
        for vs in Vs:
            # vs: iが書き込める場所(bit)
            
            for state, v in pd.items():
                if Bit[vs] & state:
                    continue
                if f(vs, state):
                    nd[state | Bit[vs]] += v % mod
        pd = nd
    print(sum(pd.values()) % mod) 
    return

#Solve
if __name__ == '__main__':
    D()