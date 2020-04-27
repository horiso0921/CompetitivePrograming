N, K = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)
ans = 0
for i in range(K):
    ans += l[i]
print(ans)