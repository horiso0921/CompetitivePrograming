def dfs(sum1,sum2,i):
    if i != N:
        bf1 = dfs(sum1+t[i],sum2,i+1)
        bf2 = dfs(sum1,sum2+t[i],i+1)
        return min(bf1, bf2)
    else:
        return max(sum1, sum2)

N = int(input())
t = []
sum1 , sum2 = 0, 0

for i in range(N):
    a = int(input())
    t.append(a)
print(dfs(0,0,0))