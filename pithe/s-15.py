# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def ABC(k,s):
	size = 3*((2**k)-1)
	if (k == 1):
		if(s == 1):
			return "A"
		elif(s == 2):
			return "B"
		elif(s == 3):
			return "C"
	elif(s==1):
		return "A"
	elif(s==size):
		return "C"
	elif((size+1)/2 == s):
	    return "B"
	elif((size+1)/2 > s):
		return ABC(k-1, s-1)
	elif((size+1)/2 < s):
		return ABC(k-1, s-((size+1)/2))
kst = input()
kst = kst.split()
kst = list(kst)
k = int(kst[0])
s = int(kst[1])
t = int(kst[2])

for i in range(s, t+1):
	print(ABC(k,i), end="")