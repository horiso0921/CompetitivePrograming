#A
"""
x, y = map(int, input().split())
print(y//x)
"""

#B
"""
n = int(input())
ans = [int(input()) for _ in range(n)]
print(min(ans))
"""

#C
"""
t = int(input())
n = int(input())
ab = list(map(int, input().split()))
m = int(input())
bb = list(map(int, input().split()))
import queue
ai = queue.Queue()
for i in range(n):
    ai.put(ab[i])
bi = queue.Queue()
for i in range(m):
    bi.put(bb[i])
hito = bi.get()

while not ai.empty():
    
    if m > n:
        print("no")
        break

    tako = ai.get()
    

    if tako > hito:
        print("no")
        break
    
    elif tako + t >= hito:
        if bi.empty():
            print("yes")
            break
        hito = bi.get()

else:
    print("no")

"""

#D
n = int(input())
feild = [list(map(int, input().split())) for i in range(n)]
num_tenin = int(input())
tenin = [int(input()) for i in range(num_tenin)]

ans = [0 for i in range(n ** 2 + 1)]

dp = [[0 for i in range(n+1)] for k in range(n+1)]
for i in range(n):
    for k in range(n):
        dp[k][i] = dp[k - 1][i] + dp[k][i - 1] - dp[k - 1][i - 1] + feild[k][i]
        ans[(k+1)*(i+1)] = max(ans[(k+1)*(i+1)], dp[k][i])

for tate in range(n):
    for yoko in range(n):
        for tate_haba in range(1, n - tate + 1):
            for yoko_haba in range(1, n - yoko + 1):
                bf = dp[tate + tate_haba - 1][yoko + yoko_haba - 1] - dp[tate - 1][yoko + yoko_haba - 1] - dp[tate + tate_haba - 1][yoko - 1] + dp[tate - 1][yoko - 1]
                ans[yoko_haba * tate_haba] = max(ans[tate_haba * yoko_haba], bf)
                for i in range(1, n ** 2 + 1):
                    ans[i] = max(ans[i], ans[i - 1])
for ten in tenin:
    print(ans[ten])