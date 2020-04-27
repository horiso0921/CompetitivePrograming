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
    n = S()
    for i in n:
        if i == "1":
            print(9, end="")
        else:
            print(1, end="")
    print()
    return

#B
def B():
    n = II()
    for i in range(111, 1000, 111):
        if n <= i:
            print(i)
            return
    return

#C
def C():
    return

# D
# 解説AC
# 参考: https://atcoder.jp/contests/abc111/submissions/6425569
# 天才か？
# 和の偶奇にしか気づけなかった
def D():
    n = II()
    xy = LIR(n)
    xy_ = [a + b for a, b in xy]
    RULD = ["R", "U", "L", "D"]
    R = 0
    if len(set(map(lambda x: x & 1, xy_))) == 2:
        print(-1)
        return
    ans = [1 << i for i in range(33)]
    f = (xy[0][0] + xy[0][1]) & 1 ^ 1
    if f: ans = [1] + ans
    xy = [[abs(x - f), abs(y), ((x - f) < 0) << 0 | (y < 0) << 1] for x, y in xy]
    lis = []
    for x, y, p in xy:
        b = (x & 1) ^ 1
        tmp = [b]
        for i in range(1,33):
            if b == R:
                if x >> i & 1:
                    if y >> i & 1:
                        k = i
                        while x >> k & 1:
                            x ^= 1 << k
                            k += 1
                        x ^= 1 << k
                        tmp[-1] ^= 2
                        b ^= 1
                        tmp.append(b)
                    else:
                        tmp.append(b)
                else:
                    if y >> i & 1:
                        b ^= 1
                        tmp.append(b)
                    else:
                        tmp[-1] ^= 2
                        tmp.append(b)
            else:
                if y >> i & 1:
                    if x >> i & 1:
                        k = i
                        while y >> k & 1:
                            y ^= 1 << k
                            k += 1
                        y ^= 1 << k
                        tmp[-1] ^= 2
                        b ^= 1
                        tmp.append(b)
                    else:
                        tmp.append(b)
                else:
                    if x >> i & 1:
                        b ^= 1
                        tmp.append(b)
                    else:
                        tmp[-1] ^= 2
                        tmp.append(b)
        for i in range(33):
            if p & 1:
                if tmp[i] & 1 ^ 1:
                    tmp[i] ^= 2
            if p & 2:
                if tmp[i] & 1:
                    tmp[i] ^= 2
        lis.append(map(lambda x: RULD[x], tmp))
    print(33+f)
    print(*ans)
    for a in lis:
        print("R"*f+"".join(a))
    return


#Solve
if __name__ == '__main__':
    D()
