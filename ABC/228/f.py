#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
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
import math
class SegTree2D():
    DEFAULT = {
        'min': 1 << 60,
        'max': 0,
        'sum': 0,
        'prd': 1,
        'gcd': 0,
        'lmc': 1,
        '^': 0,
        '&': (1 << 60) - 1,
        '|': 0,
    }

    FUNC = {
        'min': min,
        'max': max,
        'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y),
        'gcd': math.gcd,
        'lmc': (lambda x, y: (x * y) // math.gcd(x, y)),
        '^': (lambda x, y: x ^ y),
        '&': (lambda x, y: x & y),
        '|': (lambda x, y: x | y),
    }

    def __init__(self,ls2D, mode='min', func=None, default=None):
        """
        要素ls2D, 関数mode (min,max,sum,prd(product),gcd,lmc,^,&,|)
        func,defaultを指定すれば任意の関数、単位元での計算が可能
        """
        N = len(ls2D)
        M = len(ls2D[0])
        if default == None:
            self.default = self.DEFAULT[mode]
        else:
            self.default = default
        if func == None:
            self.func = self.FUNC[mode]
        else:
            self.func = func
        self.N = N
        self.M = M
        self.KN = (N - 1).bit_length()
        self.KM = (M - 1).bit_length()
        self.N2 = 1 << self.KN
        self.M2 = 1 << self.KM
        self.dat = [[self.default] * (2**(self.KM + 1)) for i in range(2**(self.KN + 1))]
        for i in range(self.N):
            for j in range(self.M):
                self.dat[self.N2 + i][self.M2 + j] = ls2D[i][j]
        self.build()

    def build(self):
        for j in range(self.M):
            for i in range(self.N2 - 1, 0, -1):
                self.dat[i][self.M2 + j] = self.func(self.dat[i << 1][self.M2 + j], self.dat[i << 1 | 1][self.M2 + j])
        for i in range(2**(self.KN + 1)):
            for j in range(self.M2 - 1, 0, -1):
                self.dat[i][j] = self.func(self.dat[i][j << 1], self.dat[i][j << 1 | 1])

    def leafvalue(self, x,y):  # (x,y)番目の値の取得
        return self.dat[x + self.N2][y + self.M2]

    def update(self, x, y, value):  # (x,y)の値をvalueに変える
        i = x + self.N2
        j = y + self.M2
        self.dat[i][j] = value
        while j > 1:
            j >>= 1
            self.dat[i][j] = self.func(self.dat[i][j << 1], self.dat[i][j << 1 | 1])
        j = y + self.M2
        while i > 1:
            i >>= 1
            self.dat[i][j] = self.func(self.dat[i << 1][j], self.dat[i << 1 | 1][j])
            while j > 1:
                j >>= 1
                self.dat[i][j] = self.func(self.dat[i][j << 1], self.dat[i][j << 1 | 1])
            j = y + self.M2
        return

    def query(self, Lx, Rx, Ly, Ry):  # [Lx,Rx)×[Ly,Ry)の区間取得
        Lx += self.N2
        Rx += self.N2
        Ly += self.M2
        Ry += self.M2
        vLx = self.default
        vRx = self.default       
        while Lx < Rx:
            if Lx & 1:
                vLy = self.default
                vRy = self.default
                Ly1 = Ly
                Ry1 = Ry
                while Ly1 < Ry1:
                    if Ly1 & 1:
                        vLy = self.func(vLy, self.dat[Lx][Ly1])
                        Ly1 += 1
                    if Ry1 & 1:
                        Ry1 -= 1
                        vRy = self.func(self.dat[Lx][Ry1], vRy)
                    Ly1 >>= 1
                    Ry1 >>= 1
                vy = self.func(vLy, vRy)
                vLx = self.func(vLx,vy)
                Lx += 1
            if Rx & 1:
                Rx -= 1
                vLy = self.default
                vRy = self.default
                Ly1 = Ly
                Ry1 = Ry
                while Ly1 < Ry1:
                    if Ly1 & 1:
                        vLy = self.func(vLy, self.dat[Rx][Ly1])
                        Ly1 += 1
                    if Ry1 & 1:
                        Ry1 -= 1
                        vRy = self.func(self.dat[Rx][Ry1], vRy)
                    Ly1 >>= 1
                    Ry1 >>= 1 
                vy = self.func(vLy, vRy)               
                vRx = self.func(vy, vRx)
            Lx >>= 1
            Rx >>= 1
        return self.func(vLx, vRx)
#solve
def solve():
    h,w,h1,w1,h2,w2 = LI()
    a = [[0]+LI()+[0]*w for i in range(h)]
    w *= 2
    for hi in range(h):
        a.append([0] * (w + 1))
    h *= 2
    acc = [[0] * (w + 1)]
    for ai in a:
        acc.append(list(itertools.accumulate(ai)))
    for hi in range(h):
        for wi in range(w+1):
            acc[hi+1][wi] += acc[hi][wi]
    ss = []
    for hi in range(h-h2+1):
        tmp = []
        for wi in range(w-w2+1):
            xx = acc[hi+h2][wi+w2] - acc[hi][wi+w2] - acc[hi+h2][wi] + acc[hi][wi]
            tmp.append(xx)
        ss.append(tmp)

    seg = SegTree2D(ss, mode='max')
    ans = 0
    maxh = h-h2
    maxw = w-w2
    
    for hi in range(h-h1+1):
        if hi > maxh: continue
        for wi in range(w-w1+1):
            xx = acc[hi+h1][wi+w1] - acc[hi][wi+w1] - acc[hi+h1][wi] + acc[hi][wi]
            if wi > maxw: continue
            tmp = seg.query(hi, max(hi+h1-h2+1,hi+1),wi, max(wi+w1-w2+1, wi+1))
            ans = max(xx-tmp, ans)
    print(ans)
            
    return


#main
if __name__ == '__main__':
    solve()