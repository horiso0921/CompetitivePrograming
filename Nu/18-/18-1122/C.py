import bisect

N,A = map(int, input().split())
x = list(map(int, input().split()))
for i in range(N):
    x[i] = x[i] - A
x.sort()

