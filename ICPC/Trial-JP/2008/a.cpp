#include <iostream>

using namespace std;

int main()
{
    int n, m, p;
    int x[100];
    int ans;
    while (1)
    {   
        cin >> n >> m >> p;
        if (n == 0 && m == 0 && p == 0){
            break;
        }
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> x[i];
            ans += x[i];
        }
        ans *= 100 - p;
        if (x[m-1] == 0){
            cout << 0 << endl;
        }
        else {
            cout << ans / x[m - 1] << endl;
        }
    }
    return 0;
}
