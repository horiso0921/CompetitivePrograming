#include <stdio.h>
#include <stdlib.h>
long long int n,k;
long long int a[200000];

int f(long long int x)
{
    long long int ai,res,ok,ng,mid;
    res = 0;
    for (int i = 0; i < n; i++)
    {
        // printf("%lld\n", res);
        ai = a[i];
        if(ai == 0){
            if(x < 0){
                res += 0;
            } else {
                res += n - 1;
            }
        } else
        {
            if(ai <= -1){
                if (ai * ai <= x){
                    res -= 1;
                }
                ok = n;
                ng = -1;
                while (ok-ng>1)
                {
                    mid = (ok + ng) / 2;
                    if(a[mid]*ai<=x){
                        ok = mid;
                    } else {
                        ng = mid;
                    }
                }
                res += n - ok;
            } else
            {
                if (ai * ai <= x)
                {
                    res -= 1;
                }
                ok = -1;
                ng = n;
                while (ng - ok > 1)
                {
                    mid = (ok + ng) / 2;
                    if (a[mid] * ai <= x)
                    {
                        ok = mid;
                    }
                    else
                    {
                        ng = mid;
                    }
                }
                res += ok + 1;
            }
            
        }
    }
    // printf("%lld\n", res);
    return k <= res / 2;
}
int asc(const void *a, const void *b)
{
    long long *A = (long long *)a;
    long long *B = (long long *)b;
    if (*A > *B)
        return 1;
    if (*A < *B)
        return -1;
    return 0;
}
int main(){
    scanf("%lld", &n);
    scanf("%lld", &k);
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", &a[i]);
    }
    qsort(a, n , sizeof(long long int), asc);
    long long int ok, ng,mid;
    ok = 1000000000000000000;
    ng = -1000000000000000000 - 1;
    while(ok - ng>1){
        mid = (ok + ng) / 2;
        if(f(mid)){
            ok = mid;
        } else {
            ng = mid;
        }
    }
    printf("%lld\n", ok);

    return 1;
}