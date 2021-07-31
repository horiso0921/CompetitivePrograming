#include <iostream>

using namespace std;
# Define N 200000
int main(int argc, char const *argv[])
{
    long int mod = 1000000007;
    int t, n, m;
    cin >> t;
    long int dp[N + 11][10] = {};
    long int dpc[N + 11] = {};
    dp[0][0] = 1;
    for (int i = 0; i < N + 10; i++)
    {
        dp[i + 1][0] = dp[i][9];
        dp[i + 1][1] = dp[i][9];
        for (int j = 0; j < 9; j++)
        {
            dp[i + 1][j + 1] += dp[i][j];
            dp[i + 1][j + 1] %= mod;
        }
        for (int j = 0; j < 10; j++)
        {
            dpc[i] += dp[i][j];
            dpc[i] %= mod;
        }
    }
    for (int i = 0; i < t; i++)
    {
        scanf("%d%d", &n, &m);
        long int x;
        long int ans = 0;
        while (n != 0)
        {
            x = n % 10;
            ans += dpc[m + x];
            ans %= mod;
            n /= 10;
        }
        printf("%ld\n", ans);
    }

    return 0;
}