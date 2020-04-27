def main():
    mod = 10 ** 9 + 7
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]

    if not m:
        print(0)
        return
    
    mx = [0] * (n + 1)
    mn = [mod] * (n + 1)
    
    for i in range(n):
        mx[i + 1] = mx[i] if mx[i] > a[i] else a[i]
        mn[n - i - 1] = mn[n - i] if mn[n - i] < a[n - i - 1] else a[n - i - 1]
    
    dp = [0, 0]
    
    dp[1] = 2
    mxi = mx[1]

    def s():
        ai = a[i]
        check0 = mx[i + 1] == ai
        check1 = mn[i + 1] >= mx[i]
        check2 = mn[i] == ai

        print(check0,check1,check2)
        if mxi1 == ai:
            if mn[i + 1] >= mxi:
                for j in range(i + 1):
                    ndp[j + 1] += dp[j] + dp[i - j]

            else:
                for j in range(i + 1):
                    ndp[j + 1] += dp[j]

        else:
            if i == n - 1 or 1:
                if mn[i] == ai:
                    for j in range(i + 1):
                        ndp[j] += dp[j]
        
        
    # print(dp)
    for i in range(1, n):

        ndp = [0] * (i + 2)
        mxi1 = mx[i+1]
        s()
        mxi = mxi1
        dp = [x % mod for x in ndp]
        print(ndp)
    ans = sum(dp[n - m:m + 1])
        

    print(ans%mod)

if __name__ == "__main__":
    main()


