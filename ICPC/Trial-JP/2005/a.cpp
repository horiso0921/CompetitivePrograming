#include <iostream>

using namespace std;

string handle[][5] = {{".", ",", "!", "?", " "},
                      {"a", "b", "c", "", ""},
                      {"d", "e", "f", "", ""},
                      {"g", "h", "i", "", ""},
                      {"j", "k", "l", "", ""},
                      {"m", "n", "o", "", ""},
                      {"p", "q", "r", "s", ""},
                      {"t", "u", "v", "", ""},
                      {"w", "x", "y", "z", ""}};
int handlenum[] = {5, 3, 3, 3, 3, 3, 4, 3, 4};

void solve()
{
    string str, tmp, ans;
    cin >> str;
    int j, l;
    l = 0;
    for (long unsigned int k = 0; k < str.size(); k++)
    {
        j = str.at(k) - '0' - 1;
        if (j == -1)
        {
            ans = ans + tmp;
            tmp = "";
            l = 0;
        }
        else
        {
            tmp = handle[j][l];
            l++;
            l = l % handlenum[j];
        }
    }
    cout << ans << endl;
}

int main()
{
    int i;
    cin >> i;
    for (int j = 0; j < i; j++)
    {
        solve();
    }
}
