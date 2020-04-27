def DFS(CHECK, r, c, k, SAVE,ans):
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    for i in range(4):
        PL = MAP[r+x[i]][c+y[i]]
        if PL == '.':
            DFS(CHECK, r+x[i], c+y[i], k, SAVE,ans+1)
        elif PL == 'T':
            continue
        elif PL == 'E':
            if k == 5:
                return DFS(CHECK,r,c,k,SAVE,ans) 

R,C,K = map(int, input().split())
MAP = []
MAP.append(["T" for i in range(C+2)])
CHECK = [[0 for i in range(C)] for k in range(R)]
for i in range(R):
    MAP.append("T"+input()+"T")
MAP.append(["T" for i in range(C+2)])
print(MAP)
SAVE = [0 for i in range(K)]
for i in range(R+2):
    for k in range(C+2):
        if MAP[i][k] == 'S':
            print(DFS(CHECK, i, k, 0,SAVE,0))