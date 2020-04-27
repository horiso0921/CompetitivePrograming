#A
"""
n = int(input())
print(2*n)
"""

#B
"""
a1 = list(map(str, input().split()))
a2 = list(map(str, input().split()))
a3 = list(map(str, input().split()))
a4 = list(map(str, input().split()))

ans = []
ans.append(a1)
ans.append(a2)
ans.append(a3)
ans.append(a4)

for i in range(3,-1,-1):
    for k in range(3,-1,-1):
        print(ans[i][k], end=" ")
    print()
"""

#C
"""
n = int(input())
n = n % 30
ans = ["123456"]
for i in range(30):
    ansb = list(ans[i])
    ansb[i % 5] = ans[i][i % 5 + 1]
    ansb[i % 5 + 1] = ans[i][i % 5]
    ansc = ""
    for k in range(6):
        ansc += ansb[k]
    ans.append(ansc)
print(ans[n])
"""

#D

r, g, b = map(int, input().split())

ans = float("INF")

#Gの左の場所を仮定する
for left_G in range(-500, 500):
    
    right_G = left_G + g - 1

    bf = 0

    #G
    for G in range(left_G, right_G + 1):
        bf += abs(G)
    
    #R
    # -100 (r-1)//2
    #   |   |
    #RRRRRRRRGGGGGG  
    if left_G > (r - 1) // 2 - 100:
        if r % 2 == 1:
            bf += (r ** 2 - 1) // 4
        else:
            bf += r ** 2 // 4
    # -100→(r-1)//2
    #   |   |
    #RRRRRRGGGGGGGG
    else:
        for R in range(left_G - r + 100, left_G + 100):
            bf += abs(R)
    
    #B
    #(b-1)//2←100
    #   |      |
    #GGBBBBBBBBBBB  
    if right_G < 100 - (b - 1) // 2:
        if b % 2 == 1:
            bf += (b ** 2 - 1) // 4
        else:
            bf += b ** 2 // 4
    #(b-1)//2←100
    #   |      |
    #GGGGGGGGBBBBB
    else:
        for B in range(right_G + 1 - 100, right_G + 1 + b - 100):
            bf += abs(B)

    ans = min(ans, bf)

print(ans)

#DP PyPyでは通らなかった
"""
def count(hidari, kosuu):
    if kosuu <= r:
        return abs(400 - hidari)
    elif kosuu <= r + g:
        return abs(500 - hidari)
    else:
        return abs(600 - hidari)
 
#左端-500を0とする

dp = [[float("INF") for i in range(r+g+b+1)] for _ in range(900)] 

for i in range(900):
    dp[i][0] = 0 

for i in range(1, 900):
    for k in range(1, r + g + b + 1):
        dp[i][k] = min(dp[i - 1][k - 1] + count(i, k), dp[i - 1][k])

print(dp[-1][-1])
"""