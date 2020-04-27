
# -*- coding: utf-8 -*-
# 文字列の入力

Nz, Nb = map(int, input().split())

Ai = map(int, input().split())
Bi = map(int,input().split())

Ai = list(Ai)
Bi = list(Bi)

Ai.sort()
Bi.sort()

SUM = 0
AVE = 0

ai = 0
bi = 0


while(1):

	if(ai == Nz-1 and bi == Nb-1):
		if(Ai[ai] == Bi[bi]):
			AVE += 1
			SUM += 1
		else:
			SUM += 2
		break
	if(ai == Nz ):
		ai -= 1
	if(bi == Nb):
		bi -= 1
	if(Ai[ai] == Bi[bi]):
		AVE += 1
		SUM += 1
		ai += 1
		bi += 1
	elif(Ai[ai] > Bi[bi]):
		SUM += 1
		bi += 1
		if(bi == Nb):
			bi -= 1
			ai += 1
	elif(Ai[ai] < Bi[bi]):
		SUM += 1
		ai += 1
		if(ai == Nz ):
			ai -= 1
			bi += 1

print(AVE/SUM)