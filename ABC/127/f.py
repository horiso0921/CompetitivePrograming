
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
def F():
    q = II()
    small = []
    big = []
    len_small = 0
    len_big = 0
    ans = 0
    for i in range(q):
        query = LI()

        if query[0] == 1:
            a, b = query[1:3]
            ans += b
            if len_small == 0:
                heappush(small, -a)
                len_small += 1
                continue
            if len_big == 0:
                num_small = -heappop(small)
                lis = [a, num_small]
                lis.sort()
                heappush(small, -lis[0])
                heappush(big, lis[1])
                len_big += 1
                if lis[0] == a:
                    ans += num_small - lis[0]
                else:
                    ans += (a - num_small)
                continue
            num_small = -heappop(small)
            num_big = heappop(big)
            lis = [a, num_big, num_small]
            lis.sort()
            if len_big != len_small:
                heappush(small, -lis[0])
                heappush(big, lis[1])
                heappush(big, lis[2])
                if lis[0] == a:
                    ans -= (num_small - a) * (len_small - 1)
                    ans += (num_small - a) * (len_big + 1)
                else:
                    ans += a - num_small
                len_big += 1
            else:
                heappush(small, -lis[0])
                heappush(small, -lis[1])
                heappush(big, lis[2])
                if lis[0] == a:
                    ans += num_small - a
                elif lis[1] == a:
                    ans += (a - num_small) * len_small
                    ans -= (a - num_small) * len_big
                else:
                    ans += (num_big - num_small) * len_small
                    ans -= (num_big - num_small) * len_big
                    ans += a - num_big
                len_small += 1

        else:
            a = -small[0]
            print(a, ans)
    return


