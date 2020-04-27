
# -*- coding: utf-8 -*-
# 文字列の入力
import math

A, B = map(int, input().split())

prime = []
for i in range(int(math.sqrt(A)))
	prime.append(0)
	
	
for i in range(B+2, A+1):
	flg = 0
	for j in range(2,i):
		if(i%j == 0):
			i = i/j
			prime[i] += 1
			flg = 1
	if(flg == 0):
		prime[]