"""
N = int(input())

import math

al = [list(map(int, input().split())) for i in range(N)]
keta = [0 for i in range(N)]
keta10 = [0 for i in range(N)]
keta10[N-1] = 1
B = int(input())
amariB = 10 ** 5 % B

for i in range(N - 1, 0, -1):

    keta[i-1] = (al[i][1] * int(math.log10(al[i][0]) + 1))
    if keta[i - 1] > (10 ** 5):
        bfketa = keta[i - 1]
        syoketa = bfketa // (10 ** 5)
        amariketa = bfketa % (10 ** 5)
        bffketa = (amariB ** syoketa )%B
        bffketa = (bffketa * (10 ** amariketa)) % B
    else:
        bffketa = (10 ** keta[i - 1]) % B
    keta10[i - 1] = (bffketa * keta10[i]) % B

keta10[N-1] = 1
ans = 0
ansb = 0

for i in range(N):
    if al[i][1] > 10**5:
        abb = str(al[i][0])
        abbb = abb
        for k in range(10**5):
            abb += abbb	
        ab = int(abb) % B
        abb = str(al[i][0])
        abd = abb
        kaisuu = al[i][1]
        kaisuusyo = kaisuu // 10**5
        kaisuuamari = kaisuu % 10 ** 5
        for k in range(kaisuuamari):
            abd += abb
        abd = int(abd) % B
        abketa = (10 ** 5) * int(math.log10(al[i][0]) + 1)
        abketa10 = abketa % B
        abketa10b = abketa10
        ansb = ab
        for k in range(kaisuusyo-1):
            ansb = (ansb + ((ab * abketa10) % B))
            abketa10 = (abketa10b*abketa10) % B
        ansb += abketa10 * abd
        ansb = ansb * keta10[i]
        ansb = ansb % B
        
    else:
        abb = str(al[i][0])
        abd = abb
        for k in range(al[i][1] - 1):
            abd += abb
        abd = int(abd) % B
        ansb = (abd * keta10[i]) % B
        print(abb)
    ans += ansb               
    ans = ans % B
    


print(ans)
"""
"""
import time

start = time.time()
a = 1
for i in range(10**3):
    a = (a * ((10 ** 1000000) % 1000000007)) % 1000000007
print(a)

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
"""

