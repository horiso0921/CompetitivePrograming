#A
"""
a, b, c = map(int, input().split())
print(min(b//a, c))
"""
#B
"""
a, b, k = map(int, input().split())
for i in range(max(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        k -= 1
        if k == 0:
             print(i)
"""

#C
"""
s = list(input())
an0 = 0
an1 = 0
for i in s:
    if i == "1":
        an1 += 1
    if i == "0":
        an0 += 1
print(min(an0, an1)*2)
"""

#D

n, m = map(int, input().split())
ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))

ab = ab[-1::-1]
size = [1 for _ in range(n)]
height = [1 for _ in range(n)]
par = [i for i in range(n)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def union(x, y):
    s1 = find(x)
    s2 = find(y)
    if s1 != s2:
        if height[s1] < height[s2]:
            par[s1] = s2
            size[s2] += size[s1]
            size[s1] = 0
        else:
            par[s2] = s1
            size[s1] += size[s2]
            size[s2] = 0
            if height[s1] == height[s2]:
                height[s1] += 1
 

ans = [0 for i in range(m)]
ans[0] = n * (n - 1) // 2
for num, i in enumerate(ab):
    if num == m-1:
        break
    a = i[0] - 1
    b = i[1] - 1
    sizea = size[find(a)]
    sizeb = size[find(b)]
    if find(a) == find(b):
        ans[num + 1] = ans[num]
    else:
        ans[num + 1] = ans[num] - (sizea * sizeb)
    union(a,b)
    
    
ans = ans[-1::-1]
for i in ans:
    print(i)