#include <iostream>

using namespace std;

int main()
{
    int n, a, b, c, x, i, j, f, flag, ans;
    int y[100];
    while (1)
    {
        cin >> n >> a >> b >> c >> x;
        if (n == 0)
        {
            break;
        }
        for (i = 0; i < n; i++)
        {
            cin >> y[i];
        }
        ans = -1;
        j = 0;
        for (i = 0; i < 10001; i++)
        {
            flag = 1;
            if (x == y[j])
                j++;
            if (j == n)
            {
                ans = i;
                break;
            }
            x = (a * x + b) % c;
        }
        cout << ans << endl;
    }
    return 0;
}
