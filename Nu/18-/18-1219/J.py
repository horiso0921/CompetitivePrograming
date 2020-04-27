n, m = map(int, input().split())
ans = ["second", "first"]
if m == 0:
    print(ans[n % 2])
elif m * 2 + 1 > n:
    print("first")
else:
    a = 0