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
    while True:
        n,m = LI()
        if n == 0 and m == 0:
            break
        road = [[] for i in range(n)]
        bit = [0 for i in range(n)]
        done = [True for i in range(n)]
        for _ in range(m):
            u, v = LI_()
            road[u].append(v)
            road[v].append(u)
            if done[u]:
                done[u] = False
                if done[v]:
                    bit[u] = bit[v] ^ 1
                    done[v] = False
                else:
                    bit[u] = bit[v] ^ 1
            else:
                if done[v]:
                    done[v] = False
                    bit[v] = bit[u] ^ 1
            print(bit)
        ans = []
        for num,i in enumerate(road):
            for k in i:
                if bit[k] == bit[num]:
                    break
            else:
                continue
            break
        else:
            if bit.count(1) % 2:
                ans.append(bit.count(1))
                
        print(road,bit)

    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    A()
