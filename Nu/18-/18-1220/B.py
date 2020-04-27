a = []
for i in range(10):
    a.append(list(input()))
ans = [0 for i in range(10)]
for i in range(10):
    for k in range(10):
        if a[i][k] == "o":
            ans[k] = 1
for i in range(10):
    if ans[i] == 0:
        print("No")
        break
else:
    print("Yes")