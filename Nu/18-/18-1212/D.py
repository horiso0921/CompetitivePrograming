X = input()
s = list(input())

a = s.count(X)
ans = ""
for i in range(a):
    s.remove(X)
for i in range(len(s)):
    ans += s[i]
print(ans)