N = int(input())
w = list(map(str, input().split()))
A = ["TAKAHASHIKUN", "Takahashikun", "takahashikun","TAKAHASHIKUN.", "Takahashikun.", "takahashikun."]
ans = 0
for i in range(N):
    if w[i] in A:
        ans += 1
print(ans)