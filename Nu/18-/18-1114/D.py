S = input().lower()
A = ["i","c","t"]
a = 0
AN = 1
ans = ["YES", "NO"]
for i in range(len(S)):
    if S[i] == A[a]:
        a += 1
        if a == 3:
            AN = 0
            break
print(ans[AN])

            