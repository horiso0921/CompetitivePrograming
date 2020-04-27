# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def AC(n, fld, m, pi, fldx):
	for i in range(n):
		for k in range(n):
			if(m > n*n):
				return False
			#print(i,k)
			if(fld[i][k] == pi[0]):
				a = 0
				if(ckc(n, fld, m, pi, i, k, a, fldx)):
				    for i in range(n*n):
				        fldx[i] = 'false'
				    return True
	return False
				
def ckc(n, fld, m, pi, i, k, a, fldx):
	#print(fldx)
	#print(i, k, a, m)
	
	if (a == m-1):
	    return True
	a += 1
	fldx[i*n+k] = 'True'
	#print(fldx)
	if(k == 0):
		if(fld[i][k+1] == pi[a] and fldx[i*n+k+1] == 'false'):  
			if(ckc(n, fld, m, pi, i, k+1, a, fldx)):
			    return True
		if(i == 0):
			if(fld[i+1][k] == pi[a] and fldx[(i+1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i+1, k, a, fldx)):
				    return True
		if(i == n-1):
			if(fld[i-1][k] == pi[a] and fldx[(i-1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i-1, k, a, fldx)):
				    return True
		if(0 < i and i < n-1):
			if(fld[i+1][k] == pi[a] and fldx[(i+1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i+1, k, a, fldx)):
				    return True
			if(fld[i-1][k] == pi[a] and fldx[(i-1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i-1, k, a, fldx)):
				    return True
	if(k == n-1):
		if(fld[i][k-1] == pi[a] and fldx[i*n+k-1] == 'false'):
				if(ckc(n, fld, m, pi, i, k-1, a, fldx)):
				    return True
		if(i == 0):
			if(fld[i+1][k] == pi[a] and fldx[(i+1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i+1, k, a, fldx)):
				    return True
		if(i == n-1):
			if(fld[i-1][k] == pi[a] and fldx[(i-1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i-1, k, a, fldx)):
				    return True
		if(0 < i and i < n-1):
			if(fld[i+1][k] == pi[a] and fldx[(i+1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i+1, k, a, fldx)):
				    return True
			if(fld[i-1][k] == pi[a] and fldx[(i-1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i-1, k, a, fldx)):
				    return True
	if(0<k and k < n-1):
		#print("e", i ,k, fld[i-1][k], pi[a], n)
		if(fld[i][k+1] == pi[a] and fldx[i*n+k+1] == 'false'):
		#	print("1")
			if(ckc(n, fld, m, pi, i, k+1, a, fldx)):
			    return True
		if(fld[i][k-1] == pi[a] and fldx[i*n+k-1] == 'false'):
		#	print("2")
			if(ckc(n, fld, m, pi, i, k-1, a, fldx)):
			    return True
		if(i == 0):
		#	print("3")
			if(fld[i+1][k] == pi[a] and fldx[(i+1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i+1, k, a, fldx)):
				    return True
		if(i == n-1):
			#print("4")
			if(fld[i-1][k] == pi[a] and fldx[(i-1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i-1, k, a, fldx)):
				    return True
		if(0 < i and i < n-1):
			#print("k")
			if(fld[i+1][k] == pi[a] and fldx[(i+1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i+1, k, a, fldx)):
				    return True
			if(fld[i-1][k] == pi[a] and fldx[(i-1)*n+k] == 'false'):
				if(ckc(n, fld, m, pi, i-1, k, a, fldx)):
				    return True
	clear(i, k, a, fldx, m, n)
	return False
	

def clear(i, k, a, fldx, m, n):
    #print("l")
    a -= 1
    fldx[i*n+k] = 'false'
    #print(i,k)
n = int(input())
fld = []
fldx = []
for i in range(n):
	ti = input()
	fld.append(ti)
	
for i in range(n*n):
	fldx.append('false')

m = int(input())

for i in range(m):
	pi = input()
	if(AC(n, fld, len(pi), pi, fldx)):
		print('yes')
	else:
		print('no')