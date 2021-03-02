#include <iostream>
#include <map>

using namespace std;

int main()
{
    string x;
    int f, ans;
    string l[15] = {"q", "w", "e", "r", "t", "g", "f", "d", "s", "a", "z", "x", "c", "v", "b"};
    string r[11] = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"};
    map<char, int> lr;
    for (int i = 0; i < 15; i++)
    {
        lr[l[i].at(0)] = 0;
    }
    for (int i = 0; i < 11; i++)
    {
        lr[r[i].at(0)] = 1;
    }
    while (1)
    {
        cin >> x;
        f = -1;
        ans = 0;
        if (x == "#")
        {
            break;
        }
        for (int i = 0; i < x.size(); i++)
        {
            if (f == -1)
            {
                f = lr[x.at(i)];
            }
            if (f != lr[x.at(i)])
            {
                f = lr[x.at(i)];
                ans++;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
