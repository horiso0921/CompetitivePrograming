#include <bits/stdc++.h>
using namespace std;

long long solve(string X, string Y, long long A, long long E, long long S, long long R, long long i) {
    vector<vector<long long>> d(X.size() + 1, vector<long long>(Y.size() + 1, -1));

    for (long long i1 = 0; i1 <= X.size(); i1++) {
        d[i1][0] = i1 * E;
    }
    for (long long i2 = 0; i2 <= Y.size(); i2++) {
        d[0][i2] = i2 * A;
    }

    for (long long i1 = 1; i1 <= X.size(); i1++) {
        if (X.size() - i + 1 == i1){
            E = E - R;
        }
        for (long long i2 = 1; i2 <= Y.size(); i2++) {
            long long replace_cost = (X[i1 - 1] != Y[i2 - 1] ? S : 0);

            d[i1][i2] = min({
                d[i1 - 1][i2] + E,                 // 削除
                d[i1][i2 - 1] + A,                 // 挿入
                d[i1 - 1][i2 - 1] + replace_cost,  // 置き換え
            });
        }
    }

    return d[X.size()][Y.size()];
}

int main() {
    string X, Y;
    while (true) {
        cin >> X;
        if (X == "#") break;
        cin >> Y;

        long long A, E, S, R;
        cin >> A >> E >> S >> R;

        long long ans = numeric_limits<long long>::max();
        for (long long i = 0; i < X.size(); i++) {
            ans = min(ans, i * R + solve(X, Y, A, E, S, R, i));
            rotate(X.begin(), X.begin() + 1, X.end());
        }

        cout << ans << endl;
    }
}
