N, M = map(int, input().split())
C = []
for i in range(N):
    a = int(input())
    C.append(a)
    if i == 0:
        MIN = a
        I = 0
    else:
        if(a < MIN):
            C[I] = MIN
            I = i
            MIN = a
            C[i] = 0

for i in range(M):
    A, B, R = map(int, input().split())
    C[A-1] = min(C[A-1], R)
    C[B-1] = min(C[B-1], R)

SUM = MIN
for i in range(N):
    if(C[i] != 0):
        SUM += C[i]
print(SUM)