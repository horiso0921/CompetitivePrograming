#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int d, e, x, y;
    double ans;
    while (1)
    {
        cin >> d >> e;
        if (d == 0 && e == 0)
            break;
        ans = 1000000000;
        for (x = 0; x <= d; x++)
        {
            y = d - x;
            if (ans > abs(sqrt(x * x + y * y) - e))
            {
                ans = abs(sqrt(x * x + y * y) - e);
            }
        }
        cout << ans << endl;
    }
    return 0;
}
