# -*- coding: utf-8 -*-
# 文字列の入力

def bfs(i,k,n,CHECK,CLS):
    if(0 > i or i > 9 or k > 9 or 0 > k ):
        return 0
    if(CHECK[i][k] == 1):
        return 0
    if(MAP[i][k] == "x"):
        return 0
    else:
        CHECK[i][k] = 1
        CLS[i][k] = n
        bfs(i+1,k,n,CHECK,CLS)
        bfs(i-1,k,n,CHECK,CLS)
        bfs(i,k+1,n,CHECK,CLS)
        bfs(i,k-1,n,CHECK,CLS)
def CHK(i,k,n,CLS):
    if(0 > i or i > 9 or k > 9 or 0 > k ):
        return 0
    else:
        a = [CL(i+1,k,CLS),CL(i-1,k,CLS),CL(i,k+1,CLS),CL(i,k-1,CLS)]
        au = []
        for x in a:
            if x not in au:
                au.append(x)
        au.remove(0)
        if(len(au) == n-1):
            return 1
        else: return 0
def CL(i,k,CLS):
    if(0 > i or i > 9 or k > 9 or 0 > k ):
        return 0
    else:
        return CLS[i][k]



MAP = []
CHECK = []
CLS = []
for i in range(10):
    MAP.append(input())
    CHECK.append([0,0,0,0,0,0,0,0,0,0])
    CLS.append([0,0,0,0,0,0,0,0,0,0])
n = 1
for i in range(10):
    for k in range(10):
        if(CHECK[i][k] == 0 and MAP[i][k] == "o"):
            if(CHECK[i][k] == 0):
                bfs(i,k,n,CHECK,CLS)
                n += 1
if(len(CLS)>=5):
    print("NO")
    quit()
else:
    for i in range(10):
        for k in range(10):
            ANS = []
            if(MAP[i][k] == "x"):
                if(CHK(i,k,n,CLS)):
                    print("YES")
                    quit()
print("NO")
