N = int(input())
ans = 0
for i in range(N):
    ab = list(map(int, input().split()))
    ans += ab[0] * ab[1]
print(int(ans*1.05))