A = [[0,0,0,0,0,0]]
for i in range(4):
    a = [0]
    a += list(map(int, input().split()))
    a.append(0)
    A.append(a)
A.append([0,0,0,0,0,0])
flg = 0
ans = ["GAMEOVER","CONTINUE"]

for i in range(1,5):
    for k in range(1,5): 
        if A[i][k] == A[i][k+1] or A[i][k] == A[i][k-1] or A[i][k] == A[i-1][k] or A[i][k] == A[i+1][k]:
                flg = 1
        
print(ans[flg])