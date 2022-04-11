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
class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        """
        :param int size:
        """
        self.bit = [0 for _ in range(size)]
        self.size = size

    def add(self, i, w):
        """
        i番目にwを加える
        :param int i:
        :param int w:
        :return:
        """
        x = i + 1
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        """
        [0,i]の合計
        :param int i:
        :return:
        """
        res = 0
        x = i + 1
        while x > 0:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def search(self, x):
        """
        二分探索。和がx以上となる最小のインデックス(>= 1)を返す
        :param int x:
        :return :
        """
        i = 0
        s = 0
        step = 1 << self.size.bit_length()
        while step:
            if i + step <= self.size and s + self.bit[i + step - 1] < x:
                i += step
                s += self.bit[i - 1]
            step >>= 1
        return i

    def __len__(self):
        return self.size
#solve
def solve():
    n,m = LI()
    a = LI()
    b = LI()
    c = LI()
    d = LI()
    ab = [(a,b) for a,b in zip(a,b)]
    cd = [(c,d) for c,d in zip(c,d)]
    ll = sorted(set(b + d))
    dd = defaultdict(int)
    for i, l in enumerate(ll):
        dd[l] = i
    Bit = BinaryIndexedTree(len(ll) + 10)
    ab.sort(reverse=True)
    cd.sort(reverse=True)
    j = 0
    cand = []
    xx = 0
    for a,b in ab:
        for j in range(j, m):
            c,d = cd[j]
            if c >= a:
                Bit.add(dd[d], 1)
                xx += 1
            else:
                break
            j += 1
        score = Bit.sum(dd[b]-1)
        ss = xx - score
        if ss == 0:
            print("No")
            return
        ss = Bit.search(score + 1)
        Bit.add(ss, -1)
        xx -= 1
    print("Yes")
      
    return


#main
if __name__ == '__main__':
    solve()