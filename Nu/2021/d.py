#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def II(): return int(input())
mod = 1000000007

from functools import lru_cache 

@lru_cache(None)
def dfs(k, re):
    if k < 10:
        return (re + k) // d - re // d 
    
    k, r = divmod(k, 10)
    res = dfs(k, re) + (re + 9) // d - re // d 
    for _ in range(1, r+1):
        re += 1
        res += dfs(k, re)
        res %= mod
    for _ in range(r+1, 10):
        re += 1
        res += dfs(k-1, re)
        res %= mod

    return res
    

k = II()
d = II()
print(dfs(k,0))
