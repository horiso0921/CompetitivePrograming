#A

"""
n = int(input())
print((n + 1) // 2)
"""

#B
"""
n = int(input())
a = [int(input()) for i in range(n)]
a = list(set(a))
a.sort(reverse = True)
print(a[1])
"""

#C
"""
n, K = map(int, input().split())
s = list(input())
sb = sorted(s)
ans = []
def hantei(i, k, sb):
    ansnum = 0
    a = s[i:n]
    b = sb[::1]
    if a[0] != k:
        ansnum += 1
    del a[0]
    b.remove(k)
    for j in set(a):
        if a.count(j) > b.count(j):
            ansnum += a.count(j) - b.count(j)
    return ansnum
ansn = 0
for i in range(n):
    for k in sb:
        ansnumb = hantei(i, k, sb)
        if ansnumb + ansn <= K:
            if s[i] != k:
                ansn += 1
            sb.remove(k)
            ans.append(k)
            break

for i in ans: print(i, end="")
print()
"""

#D
K, m = map(int, input().split())
def productmatric(C,D):
    res = [[0 for i in range(K)] for k in range(K)]
    for i in range(K):
        for k in range(K):
            bf = 0
            for l in range(K):
                bf = bf ^ (C[i][l] & D[l][k])
            res[i][k] = bf
    return res
            

def powmatric(n, C, D):
    if n % 2:
        return powmatric(n // 2, productmatric(C, D), productmatric(D, D))
    else:
        if n == 0:
            return C
        return powmatric(n // 2, C, productmatric(D,D))
        
a = list(map(int, input().split()))
ak = []
for i in a:
    ak.append([i])
C = [list(map(int, input().split()))]
ak = ak[::-1]
for i in range(1, K):
    bfc = []
    for p in range(K):
        if i-1 == p:
            bfc.append(2 ** 32 - 1)
        else:
            bfc.append(0)
    C.append(bfc)
tani = [[0 for i in range(K)] for k in range(K)]
for i in range(K):
    tani[i][i] = 2 ** 32 - 1

if m <= K:
    print(a[m - 1])
    quit()
C = powmatric(m - K,tani, C)
ANS = 0
for i in range(K):
    ANS = ANS ^ (C[0][i] & ak[i][0])
print(ANS)
