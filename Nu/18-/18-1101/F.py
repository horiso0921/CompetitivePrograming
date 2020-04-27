import math

A,B = map(int, input().split())

N = int(input())
ANS = []
for i in range(N):
    C, D = map(int, input().split())
    if(min(C, D) >= min(A,B) and max(C,D) >= max(A,B)):
        ANS.append("YES")
    elif(C==D):
        if(A+B <= C*math.sqrt(2)):
            ANS.append("YES")
        else:
            ANS.append("NO")
    else:
        ANS.append("NO")
for i in range(len(ANS)):
    print(ANS[i])