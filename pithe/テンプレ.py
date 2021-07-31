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
inf = float(INF)
def LI(): '12 23 → [12, 23]'
	return list(map(int, stdin.readline().split()))
def LF(): '12.3 32.1 → [12.3, 32.1]'
	return list(map(float, stdin.readline().split()))
def LI_(): '12 23 → [11, 22]'
	return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): '12.3 → 12'
	return int(stdin.readline())
def IF(): '12.3 →12.3'
	return float(stdin.readline())
def LS(): 'abc acb → [["a", "b", "c"], ["a","c","b"]]'
	return list(map(list, stdin.readline().split()))
def S(): 'abc → ["a","b","c"]'
	return list(stdin.readline().rstrip())
def IR(n): """123
			  123    → [123, 123]"""
	return [II() for _ in range(n)]
def LIR(n): """123 123
			   123 123 → [[123, 123], [123, 123]]"""
	return [LI() for _ in range(n)]
def FR(n): """123.3
			  123.3 → [123.3, 123.3]"""
	return [IF() for _ in range(n)]
def LFR(n): """123.3 123.3
			   123.3 123.3 →[[123.3, 123.3], [123.3, 123.3]]"""
	return [LI() for _ in range(n)]
def LIR_(n): """123 123
				123 123 →[[122,122], [122, 122]]"""
	return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007

# A
def A():
    return

# B
def B():
    return

# C
def C():
    return

# D
def D():
    return

# E
def E():
    return

# F
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
