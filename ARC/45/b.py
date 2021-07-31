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
def solve():
    def init_min(init_min_val):
        #set_val
        for i in range(n):
            seg_min[i+num_min-1] = init_min_val[i]
        # Built
        for i in range(num_min-2, -1, -1):
            seg_min[i] = min(seg_min[2*i+1], seg_min[2*i+2])


    def update_min(k, x):
        k += num_min-1
        seg_min[k] = x
        while k:
            k = (k-1)//2
            seg_min[k] = min(seg_min[k*2+1], seg_min[k*2+2])


    def query_min(p, q):
        if q <= p:
            return ide_ele_min
        p += num_min-1
        q += num_min-2
        res = ide_ele_min
        while q-p > 1:
            if p & 1 == 0:
                res = min(res, seg_min[p])
            if q & 1 == 1:
                res = min(res, seg_min[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = min(res, seg_min[p])
        else:
            res = min(min(res, seg_min[p]), seg_min[q])
        return res


    #####単位元######
    ide_ele_min = 10**10

    
    n,m = LI()
    st = LIR_(m)
    #num_min:n以上の最小の2のべき乗
    num_min = 2**n.bit_length()
    seg_min = [ide_ele_min] * 2 * num_min
    
    imos = [0] * (n + 1)
    for s, t in st:
        imos[s] += 1
        imos[t + 1] -= 1
    for i in range(n):
        imos[i+1] += imos[i]
    init_min(imos)
    ans = []
    for i, (s, t) in enumerate(st):
        if query_min(s, t + 1) > 1:
            ans.append(str(i + 1))
    print(len(ans))
    if len(ans):
        print("\n".join(ans))
    return


#main
if __name__ == '__main__':
    solve()
