N = int(input())
S = list(input())
ans = 0
for i in range(1,N+1):
    ANS = []
    ANSB = []
    b = 0
    for k in range(i):
        ANS.append(S[k])
    ANS = list(set(ANS))
    for k in range(i,N):
        ANSB.append(S[k])
    ANSB = list(set(ANSB))
    for k in ANSB:
        if k in ANS:
            b += 1
    ans = max(ans,b)
print(ans)
            
