def main():
    n,q = map(int, input().split())
    if n == 0: return False
    par = [i for i in range(n)]
    check = [0] * n
    check[0] = 1
    for i in range(n-1):
        x = int(input())
        par[i+1] = x-1
    ques = [None] * q
    for i in range(q-1,-1,-1):
        que = input().split()
        if que[0] == "M":
            check[int(que[1]) - 1] += 1
        ques[i] = que
    
    def root(x):
        q = []
        while 1:
            if check[x]: break
            q.append(x)
            x = par[x]
        for i in q:
            par[i] = x
        return x
    ans = 0
    for q, i in ques:
        i = int(i) - 1
        if q == "M":
            check[i] -=1
        else:
            ans += root(i) + 1
    print(ans)
    return True

while main(): 
    pass
