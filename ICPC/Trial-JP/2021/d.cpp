#include <iostream>
using namespace std;


void solve(string n){
    int lens = n.length();
    int mod = 1000000007;
    int base = 2009;
    int pw[lens+1];
    for (int i = 0; i < lens+1; i++)
    {
        pw[i] = 1;
    }
    int v = 1;
    for (int i = 0; i < lens; i++)
    {
        v = v * base % mod;
        pw[i+1] = v;
    }
    
    int l = s.length();
    int h[l + 1]
    v = 0
    
    for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        return h
    def get(h, l, r):
        return (h[r] - h[l] * pw[r-l]) % mod

    dp = [inf] * (lens+1)
    dp[0] = 0
    ls = s[:lens]
    rs = s[-lens:]
    lss = ls
    rss = rs
    ls = rolling_hash(ls)
    rs = rolling_hash(rs)

    for l in range(1, lens+1):
        score = dp[l-1]
        if lss[l-1] == rss[-l]:
            if dp[l] > score:
                dp[l] = score
        for r in range(l+1, lens+1):
            zen = get(ls, l-1, r)
            kou = get(rs, lens-r, lens-l+1)
            if zen == kou:
                if dp[r] > score + (r - l + 1) ** 2:
                    dp[r] = score + (r - l + 1) ** 2

    if dp[-1] == inf:
        print(-1)
    else:
        print(dp[-1],flush=True) 
}

int main(){
    while (1)
    {
        string n;
        cin >> n;
        if (n == "#"){
            break;
        }
        solve(n);
    }
    
}