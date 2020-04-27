# -*- coding: utf-8 -*-
# 文字列の入力
import math

N = int(input())
if(N == 1):
    print("BOWWOW")
else:
    for i in range(2,N):
        if((N+1)%i == 0):
            print("BOWWOW")
            break
    else:
        for i in range(2,N):
            if((N/2)%i == 0):
                print("BOWWOW")
                break
        else:
            print("WANWAN")