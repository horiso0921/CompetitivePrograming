
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
t = int(input())
n = int(input())
ab = list(map(int, input().split()))
m = int(input())
bb = list(map(int, input().split()))
import queue
ai = queue.Queue()
for i in range(n):
    ai.put(ab[i])
bi = queue.Queue()
for i in range(m):
    bi.put(bb[i])
hito = bi.get()

while not ai.empty():
    
    if m > n:
        print("no")
        break

    tako = ai.get()
    

    if tako > hito:
        print("no")
        break
    
    elif tako + t >= hito:
        if bi.empty():
            print("yes")
            break
        hito = bi.get()

else:
    print("no")



