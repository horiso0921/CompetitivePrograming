N = int(input())
ans = []
for i in range(N):
    w = int(input())
    if i == 0:
        ans.append(w)
    else:
        for k in range(len(ans)):
            if ans[k] >= w:
                ans[k] = w
                break
        else:
            ans.append(w)
print(len(ans))