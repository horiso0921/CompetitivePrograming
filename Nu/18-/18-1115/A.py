N,M = map(int, input().split())
A = [0 for i in range(N)]
for i in range(M):
    m = list(map(int, input().split()))
    A[m[0]-1] += 1
    A[m[1]-1] += 1
for i in A:
    print(i)