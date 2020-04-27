#A 
"""
s = input()
print(s + "pp")
"""
#B
"""
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    while i % 2 == 0 or i % 3 == 2:
        i -= 1
        ans += 1
print(ans)
"""

#C
"""
txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
import math
def main():
    for i in range(n):
        x, y = map(int, input().split())
        if (math.sqrt((x - txa)** 2 + (y - tya)** 2) + math.sqrt((txb - x)** 2 + (tyb - y)** 2)) <= t * v:
            return 0
    return 1
if main():
    print("NO")
else:
    print("YES")
"""
from collections import defaultdict
#D
n, g, e = map(int, input().split())
p = list(map(int, input().split()))
abd = defaultdict(int)
abl = [[] for i in range(n+1)]
for i in range(e):
    a, b = map(int, input().split())
    abd[(a, b)] = 1
    abd[(b, a)] = 1
    abl[a].append(b)
    abl[b].append(a)

for i in p:
    abl[n].append(i)
    abl[i].append(n)
    abd[(i, n)] = 1

def zobun():
    from collections import deque
    Q = deque([])
    check = defaultdict(int)
    check[0] = 0
    Q.append((abl[0], 0))
    flg = True
    flow = float("INF")
    
    while Q and flg:   
        q0,q1 = Q.popleft()
        for q in q0:
            if not q in check and abd[(q1, q)] > 0:
                check[q] = check[q1] + 1
                if q == n:
                    flg = False
                    break               
                Q.append((abl[q], q))
    
    if flg:
        return False
    
    path = [None for i in range(check[n] + 1)]
    path[check[n]] = n
    for i in range(check[n]-1, -1, -1):
        for x in range(n + 1):
            if abd[(x, q)] > 0 and check[x] == check[q] - 1:
                path[i] = x
                flow = min(flow, abd[(x, q)])
                q = x
                break

                


    for qq in path:
        if (q, qq) in abd:
            abd[(qq, q)] += flow
            abd[(q, qq)] -= flow
            q = qq
    return True
while zobun():
    continue
ans = 0
#print(abd)
for i in abl[n]:
    ans += abd[(n,i)]
print(ans)