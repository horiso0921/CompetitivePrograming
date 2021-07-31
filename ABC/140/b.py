
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
def B():
    n = II()
    a = LI()
    b = LI()
    c = LI()
    ans = 0
    for i in range(n):
        ans += b[a[i] - 1] + (c[a[i] - 1] if i != n - 1 and a[i] + 1 == a[i + 1] else 0)
    print(ans)
    return


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
        x = i
        while x < self.size:
            self.bit[x] += w
            x += x & -x
        return

    def sum(self, i):
        """
        [0,i]の合計
        :param int i:
        :return:
        """
        res = 0
        x = i
        while x > 0:
            res += self.bit[x]
            x -= x & -x
        return res

    def search(self, x):
        """
        二分探索。和がx以上となる最小のインデックス(>= 1)を返す
        :param int x:
        :return :
        """
        ok = self.size
        ng = 0
        while abs(ok - ng) != 1:
            mid = (ok + ng)//2
            if self.sum(mid) >= x:
                ok = mid
            else:
                ng = mid
        return ok

    def __len__(self):
        return self.size

def E():
    n = II()
    a = LI()
    dic = defaultdict(int)
    for i, ai in enumerate(a):
        dic[ai] = i+1
    bit = BinaryIndexedTree(n+1)
    num = [i + 1 for i in range(n)][::-1]
    ans = 0
    for i in num:
        c = dic[i]
        L = bit.sum(c)
        bit.add(c,1)
        R = n-i-L 
        a = bit.search(L-1) if L >= 2 else 0
        b = bit.search(L) if L >= 1 else 0
        d = bit.search(L+2) if R >= 1 else n+1
        e = bit.search(L+3) if R >= 2 else n+1
        tmp = 0
        if b != 0:
            tmp += (b-a) * (d-c)
        if d != 0:
            tmp += (e-d) * (c-b)
        ans += i * tmp

    print(ans)
    return

