#include <stdio.h>
#include <stdbool.h>

int n;
long long int a[3000];
long long int dp[3001][3002][2];
bool check[3001][3002][2];
long long int f();
long long int max(long long int a, long long int b){
    return (a >= b) ? a : b;
}
long long int min(long long int a, long long int b){
    return (a <= b) ? a : b;
}

int main(int argc, char const *argv[])
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", &a[i]);
    }
    for (int i = 0; i < 3001; i++)
    {
        for (int j = 0; j < 3002; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                dp[i][j][k] = 0;
                check[i][j][k] = (i == j) ? true : false;
            }
            
        }
        
    }
    printf("%lld\n", f(0, n, 0));

    return 0;
}

long long int f(int left, int right, int tern)
{
    long long int tmp;    
    if (check[left][right][tern])
        return dp[left][right][tern];
    check[left][right][tern] = true;
    if(tern == 0){
        tmp = max(f(left + 1, right, tern ^ 1) + a[left], f(left, right - 1, tern ^ 1) + a[right - 1]);
    } else {

        tmp = min(f(left + 1, right, tern ^ 1) - a[left], f(left, right - 1, tern ^ 1) - a[right - 1]);
        
    }
    dp[left][right][tern] = tmp;
    return tmp;
}