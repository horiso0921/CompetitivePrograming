# -*- coding: utf-8 -*-
# 文字列の入力

N = input()
for i in range(len(N)//2):
    if(N[i]!=N[-i-1]):
        print("NO")
        break
else:
    print("YES")