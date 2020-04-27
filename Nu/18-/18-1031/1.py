
# -*- coding: utf-8 -*-
# 文字列の入力
import math

A, B, C = map(int, input().split())

i = C
k = 0
while(1):
    N = ((10**9)+7)*k + i
    if(N % 17 == A):
        if(N % 107== B):
            print(N)
            break
    k += 1
    