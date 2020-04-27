#!usr/bin/env python3
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

#A
def A():
    a, b = LI()
    if a <= b:
        print(a)
    else:
        print(a-1)
    return

#B
def B():
    a, b, c = LI()
    k = II()
    print(a + b + c + max(a, b, c) * ((2 ** k) - 1))
    return

#C
def C():
    H, W = LI()
    s = SR(H)
    for h in range(H):
        for w in range(W):
            if s[h][w] == "#":
                for mh, mw in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    hm = mh + h
                    wm = mw + w
                    if 0 <= hm < H and 0 <= wm < W:
                        if s[hm][wm] == "#":
                            break
                else:
                    print("No")
                    return

    print("Yes")
    return

#D
def D():
    n = II()
    ans = []
    sosu = [2]
    i = 2
    while len(ans) != n:
        for k in sosu:
            if i % k == 0:
                i += 1
                break
        else:
            sosu.append(i)
            if i % 5 == 1:
                ans.append(i)
            i += 1
    for i in ans:
        print(i, end=" ")
    print()
    return


#Solve
if __name__ == '__main__':
    B()
