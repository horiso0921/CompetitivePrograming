#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, flag, state, ans;
    string f;
    while (1)
    {
        cin >> n;
        if (n == 0)
            break;
        flag = 3;
        state = 0;
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> f;
            if (f == "lu")
                state |= 1;
            if (f == "ru")
                state |= 2;
            if (f == "ld")
                state &= 2;
            if (f == "rd")
                state &= 1;
            if (state == flag)
            {
                flag ^= 3;
                ans++;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
