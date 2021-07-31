
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

