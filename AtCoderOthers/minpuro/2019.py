# B
"""
def find(x):
    while table[x] >= 0:
        x = table[x]
    return x

def union(x, y):
    s1 = find(x)
    s2 = find(x)
    if s1 != s2:
        if table[s1] != table[s2]:
            if table[s1] < table[s2]:
                table[s2] = s1
            else:
                table[s1] = s2
        else:
            table[s1] -= 1
            table[s2] = s1
    return
    


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

ans = [0 for i in range(4)]

ans[a1-1] += 1 
ans[a2-1] += 1 
ans[a3-1] += 1 
ans[b1-1] += 1 
ans[b2-1] += 1 
ans[b3-1] += 1 

if 0 in ans or 3 in ans:
    print("NO")
else:
    print("YES")
"""

# C
k, a, b = map(int, input().split())

if a + 1 >= b:
    print(k + 1)
else:
    ans = k - 2*((k-(a-1))//2) + 1 + (b-a) * ((k - (a - 1)) // 2)
    print(ans)