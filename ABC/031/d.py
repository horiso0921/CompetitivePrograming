
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
# 数を決め打ちすればいい
# 結局DFSとやってること変わんなくねｗ

def D():
    def dfs(j):
        for num, vwi in enumerate(vw[j:]):
            v, w = vwi
            x = 0
            lw = len(w)
            for vi in v:
                vi = int(vi)
                if l[vi]:
                    lv = l[vi]
                    if ans[vi] == w[x:lv+x]:
                        x += lv
                    else:
                        return False
                    continue
                for i in range(1, 4):
                    ans[vi] = w[x:x + i]
                    l[vi] = i
                    if dfs(num + j):
                        return True
                ans[vi] = None
                l[vi] = 0
                return False
            if x != lw:
                return False
        return True

    k, n = LI()
    vw = LSR(n)
    ans = [None] * (k + 1)
    l = [0] * (k + 1)
    dfs(0)
    for i in ans[1:]:
        print("".join(i))
    return

def D_():
    k, n = LI()
    vw = LSR(n)
    lengths = itertools.product(range(1, 4), repeat=k)
    for length in lengths:
        ans = defaultdict(str)
        f = False
        for v, w in vw:
            for vi in v:
                l = length[int(vi) - 1]
                if ans[vi]:
                    if ans[vi] == w[:l]:
                        w = w[l:]
                        continue
                    else:
                        f = True
                        break
                ans[vi] = w[:l]
                w = w[l:]
            if f or w:
                break
        else:
            ans = list(ans.items())
            ans.sort()
            for _, i in ans:
                print("".join(i))
            return


    
    

