# -*- coding: utf-8 -*-
# 文字列の入力
import math

n,k = map(int, input().split())

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
    

mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
ans = 0

for i in range(1,n+1):
    ansb = 0
    for j in range(1, i+1):
        ansb += ((-1)**(i-j))*cmb(i, j, mod)*(j**n)
    ansb = ansb/math.factorial(i)
    ans += ansb%mod 
ans = ans%mod
print(int(ans))