N, L = map(int, input().split())
ans = ""
s = []
for i in range(N):
    s.append(input())

s.sort()
for i in range(N):
    ans += s[i]
print(ans)

