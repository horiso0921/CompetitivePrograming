#include <iostream>
#include <queue>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    int dp[500][500];
    int x;
    int y;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            x = min(i, j);
            y = min(n - i - 1, n - j - 1);
            dp[j][i] = min(x,y);
        }
        
    }

    int c[500][500];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            c[j][i] = 1;
        }
    }
    int ans;
    ans = 0;
    struct aa{
        int x,y;
    };

    queue<aa> que;
    aa yx;
    int score;
    int my[4] = {0, 1, 0, -1};
    int mx[4] = {1, 0, -1, 0};
    int ym;
    int xm;
    int pi;
    for (int i = 0; i < n * n; i++)
    {
        cin >> pi;
        y = pi / n;
        x = pi % n;
        ans += dp[y][x];
        c[y][x] = 0;
        yx.y = y;
        yx.x = x;
        que.push(yx);
        while (que.size())
        {
            yx = que.front();
            y = yx.y;
            x = yx.x;
            que.pop();
            score = dp[y][x] + c[y][x];
            for (int i = 0; i < 4; i++)
            {
                ym = my[i] + y;
                xm = mx[i] + x;
                if(0 < ym &&ym < n - 1 && 0 < xm &&xm < n - 1)
                {
                    if(dp[ym][xm] > score)
                    {
                        dp[ym][xm] = score;
                        yx.y = ym;
                        yx.x = xm;
                        que.push(yx);
                    }
                }
            }
            
        }
        
    }
    cout << ans << endl;
}