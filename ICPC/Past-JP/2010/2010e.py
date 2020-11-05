from collections import defaultdict

def main(n,a,s,g):
    edg = [[] for i in range(n)]
    for _ in range(a):
        x,y,lab = input().split()
        x,y = int(x),int(y)
        edg[x].append((y,lab))
    inf = "z" * 2600
    dp = [[inf] * 2600 for i in range(n)]
    dp[s][0] = ""
    d = defaultdict(lambda: defaultdict(int))
    for leng in range(2500):
        for i in range(n):
            l = dp[i][leng]
            for e,lab in edg[i]:
                if leng+len(lab) > 2500: continue
                x = l + lab
                if dp[e][leng+len(lab)] > x:
                    d[e][leng+len(lab)] = d[i][leng] | (1 << i)
                    dp[e][leng+len(lab)] = x
    ans = inf
    dpg = dp[g]    
    for i in range(2500):
        if dpg[i] < ans:
            ans = dpg[i]
    if ans == inf:
        print("NO")
        return
    for leng in range(10):
        leng += 2400
        for i in range(n):
            l = dp[i][leng]
            for e,lab in edg[i]:
                x = l + lab
                if x < ans and ((d[g][len(ans)] & (1 << e)) or (e == g)):
                    print("NO")
                    return
    print(ans)



if __name__ == "__main__":
    while 1:
        n,a,s,g = map(int, input().split())
        if n == 0: break
        main(n,a,s,g)