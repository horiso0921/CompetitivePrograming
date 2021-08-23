#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def II(): return int(input())
mod = 1000000007

from functools import lru_cache 

@lru_cache(None)
def dfs(k, re, f=1):
    if k < 10:
        if re:
            return (re + k) // d
        else:
            return (re + k) // d + f
    k, r = divmod(k, 10)
    res = dfs(k, re, f)
    for _ in range(1, r+1):
        re += 1
        re %= d
        res += dfs(k, re)
        res %= mod
    for _ in range(r+1, 10):
        re += 1
        re %= d
        res += dfs(k-1, re)
        res %= mod

    return res
k = input().rstrip()
d = II()

dp = [[0] * d for i in range(len(k))]
    

print(dfs(k,0,0))
