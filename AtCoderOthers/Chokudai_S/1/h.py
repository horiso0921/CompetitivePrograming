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
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    a = LI()

    def init_max(init_max_val):
        #set_val
        for i in range(n):
            seg_max[i+num_max-1] = init_max_val[i]
        # Built
        for i in range(num_max-2, -1, -1):
            seg_max[i] = max(seg_max[2*i+1], seg_max[2*i+2])


    def update_max(k, x):
        k += num_max-1
        seg_max[k] = x
        while k:
            k = (k-1)//2
            seg_max[k] = max(seg_max[k*2+1], seg_max[k*2+2])


    def query_max(p, q):
        if q <= p:
            return ide_ele_max
        p += num_max-1
        q += num_max-2
        res = ide_ele_max
        while q-p > 1:
            if p & 1 == 0:
                res = max(res, seg_max[p])
            if q & 1 == 1:
                res = max(res, seg_max[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = max(res, seg_max[p])
        else:
            res = max(max(res, seg_max[p]), seg_max[q])
        return res


    #####単位元######
    ide_ele_max = 0

    #num_max:n以上の最小の2のべき乗
    num_max = 2**n.bit_length()
    seg_max = [ide_ele_max] * 2 * num_max
    
    for i in a:
        x = query_max(0, i)
        update_max(i, x + 1)
    
    print(query_max(0, n + 1))
    return


#main
if __name__ == '__main__':
    solve()
