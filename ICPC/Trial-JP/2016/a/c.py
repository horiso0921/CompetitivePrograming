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
    a = S()
    b = S()
    ans = []
    i = 0
    dpsa = 0
    zooma = -1
    j = 0
    dpsb = 0
    zoomb = -1
    literal = "()[]"
    while i < len(a) and j < len(b):
        if dpsa < dpsb:
            if b[j] == "(":
                dpsb += 2
                dpsb -= dpsb & 1
            elif b[j] == ")":
                dpsb -= 1
            j += 1
        elif dpsa > dpsb:
            if a[i] == "(":
                dpsa += 2
                dpsa -= dpsa & 1
            elif a[i] == ")":
                dpsa -= 1
            i += 1
        else:
            if zooma != -1 and zoomb != -1:
                if a[i] in literal:
                    if b[j] in literal:
                        ans.append(str(zoomb+zooma))
                        ans.append(a[i])
                        zooma = -1
                        zoomb = -1
                        i += 1
                        j += 1
                    else:
                        zoomb *= 10
                        zoomb += int(b[j])
                        j += 1
                else:
                    if b[j] in literal:
                        zooma *= 10
                        zooma += int(a[i])
                        i += 1
                    else:
                        zoomb *= 10
                        zoomb += int(b[j])
                        j += 1
                        zooma *= 10
                        zooma += int(a[i])
                        i += 1
            else:
                if a[i] == b[j]:
                    if a[i] in literal:
                        ans.append(a[i])
                    else:
                        zooma = int(a[i])
                        zoomb = int(b[j])
                    i += 1
                    j += 1
                else:
                    if a[i] not in literal and b[j] not in literal:
                        zooma = int(a[i])
                        zoomb = int(b[j])
                        i += 1
                        j += 1
                    else:
                        if a[i] == "(":
                            dpsa += 2
                            ans.append(b[j])
                            i += 1
                            j += 1
                        else:
                            dpsb += 2
                            ans.append(a[i])
                            j += 1
                            i += 1
    print("".join(ans))

        





                
    return


#main
if __name__ == '__main__':
    solve()