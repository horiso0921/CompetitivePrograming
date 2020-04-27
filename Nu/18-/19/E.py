N = int(input())
A = list(map(int, input().split()))
sum = 0
for i in range(N):
    sum += A[i]
av = round(sum / N)
ans = 0
for i in range(N):
    ans += (A[i] - av)** 2
print(ans)