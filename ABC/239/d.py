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
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
#solve
def solve(a,b,c,d):
    def f(x):
        for a in range(c, d+1):
            if a + x in prime:
                return False
        return True
    for ai in range(a, b+1):
        if f(ai):
            return "Takahashi"
    return "Aoki"
    
sosu = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
        103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]

def solve_(A,B,C,D):
    '''
    高橋: 青木が選択可能な総和の範囲に素数が存在しないようにできたら勝ち
    青木: 高橋が勝てる手がなかったら勝ち

    つまり、[X+C, X+D]の範囲に素数が一つもないある値X(X in [A, B])が存在すれば高橋の勝ち
    これはすなわち、f_over(x)がxより真に大きい最小の素数を返す関数と定義した時、
    A+C-1、又は[A+C, f_over(B+C)]の範囲の素数からなる順序数列のうち、間にD-C+2以上の差が生じる連続部があればよい。
    '''
    start_index = bisect_left(sosu, A + C)
    end_index = bisect_right(sosu, B + D)
    pre_num = A+C
    print(start_index)
    print(end_index)
    if start_index == end_index:
        if pre_num not in sosu:
            return "Takahashi"
        else:
            return "Aoki"
    for i in range(start_index, end_index+1):
        if (sosu[i] - pre_num - 1) >= (D - C + 1):
            return "Takahashi"
        pre_num = sosu[i]
    return "Aoki"


#main
if __name__ == '__main__':
    for a in range(1, 101):
        for b in range(a, 101):
            for c in range(1, 101):
                for d in range(c, 101):
                    if solve_(a,b,c,d) != solve(a,b,c,d):
                        print(a,b,c,d)
                        print(solve_(a,b,c,d))
                        exit()