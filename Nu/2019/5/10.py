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
    s = S()
    i = 0
    now = 0
    ans = 0
    while i < len(s):
        if s[i] == "R":
            if now == 0:
                now += 1
                i += 1
                while i < len(s):
                    if s[i] == "R":
                        now += 1
                    else:
                        now -= 1
                    now = now % 4
                    i += 1
                    if now == 0:
                        if s[i-1] == "R":
                            ans += 1
                        break

            else:
                now += 1
                now = now % 4
                i += 1
        else:
            now -= 1
            now = now % 4
            i += 1

    print(ans)


    return

#B
def B():
    def gcd(x, y):
        x, y = max(x, y), min(x, y)
        if y != 0:
            num.append((x, y, x // y, x % y))
            return gcd(y, x % y)
        return x
    while 1:
        x, y, z = LI()
        if x == y and y == z and z == 0:
            return
        num = []
        A = gcd(x, y)
        if max(x, y) % min(x, y) == 0:
            x, y, z = x // min(x, y), y // min(x, y), z // min(x, y)
            if x > y:
                for i in range(-50001, 50001):
                    dx = x * i
                    dy = (z - x * i) / y
                    

                    
        
        ans = [1, num[-2][2]]
        i = 0
        for a, b, c, d in num[-3::-1]:
            i ^= 1
            if i:
                ans[0] += ans[1] * c
            else:
                ans[1] += ans[0] * c
        if ans[0] * x - ans[1] * y == num[-2][-1]:
            ans = [ans[0] * (z // num[-2][-1]), ans[1] * (z // num[-2][-1])]
            i = 0
            x = x // A
            y = y // A
            while True:
                if abs(ans[0] + y * (i + 1)) + abs(ans[1] + x * (i + 1)) > abs(ans[0] + y * i) + abs(ans[1] + x * i):
                    if abs(ans[0] + y * i) + abs(ans[1] + x * i) < abs(ans[0] + y *( i - 1)) + abs(ans[1] + x * (i - 1)):
                        print(abs(ans[0] + y * i), abs(ans[1] + x * i))
                        break
                    else:
                        
                        i -= 1
                else:
                    if abs(ans[0] + y * (i+1)) + abs(ans[1] + x * (i+1)) < abs(ans[0] + y *( i -1)) + abs(ans[1] + x * (i - 1)):
                        print(abs(ans[0] + y * (i+1)), abs(ans[1] + x * (i+1)))
                        break
                    else:
                        
                        i += 1
                
                    
                
        else:
            ans = [ans[1] * (z // num[-2][-1]), ans[0] * (z // num[-2][-1])]
            i = 0
            while True:
                if abs(ans[0] + y * (i + 1)) + abs(ans[1] + x * (i + 1)) > abs(ans[0] + y * i) + abs(ans[1] + x * i):
                    if abs(ans[0] + y * i) + abs(ans[1] + x * i) < abs(ans[0] + y * (i - 1) )+ abs(ans[1] + x * (i - 1)):
                        print(abs(ans[0] + y * i), abs(ans[1] + x * i))
                        return
                    else:
                        i -= 1
                else:
                    i += 1
            
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
    B()
