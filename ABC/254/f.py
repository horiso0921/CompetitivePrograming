#!/usr/bin/env python3
import sys, math
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

#####segfunc#####
def segfunc(x, y):
    if x == -1:
        return y
    if y == -1:
        return x
    while x:
        x,y = y%x,x
    return y
#################

#####ide_ele#####
ide_ele = -1
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        lres = self.ide_ele
        rres = self.ide_ele
        while l < r:
            if l & 1:
                lres = self.segfunc(lres, self.tree[l])
                l += 1
            if r & 1:
                rres = self.segfunc(rres, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return self.segfunc(lres, rres)
#solve
def solve():
    n,Q = LI()
    a = LI()
    diff_a = [abs(a[i+1] - a[i]) for i in range(n-1)]
    b = LI()
    diff_b = [abs(b[i+1] - b[i]) for i in range(n-1)]
    sa = SegTree(diff_a, ide_ele)
    sb = SegTree(diff_b, ide_ele)
    for _ in range(Q):
        h1, h2, w1, w2 = LI_()
        qa = sa.query(h1, h2)
        qb = sb.query(w1, w2)
        qab = segfunc(qa, qb)
        print(segfunc(a[h1] + b[w1], qab))

    return


#main
if __name__ == '__main__':
    solve()