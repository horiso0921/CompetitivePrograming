n = int(input())
alp = [chr(i) for i in range(97, 97+26)]
ans = []
for i in range(n):
    a = list(input())
    a.sort()
    if len(ans) > len(a):
        bf = ans
        ans = a
        a = bf
    if i == 0:
        ans = a
    else:
        k = 0
        while k < len(a):
            if k >= len(ans):
                break
            if a[k] < ans[k]:
                del a[k]
            elif a[k] == ans[k]:
                k += 1
            elif a[k] > ans[k]:
                del ans[k]

for i in ans:
    print(i, end="")