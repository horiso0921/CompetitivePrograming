#include <iostream>
#include <queue>

using namespace std;

int pow3[15];
int dp[14348907];

int check(int a, int k) {
    a = a / pow3[k];
    return a % 3;
}

int main(){
    int q, m, l, i, j, k, mask;
    string s;
    queue<int> que;
    cin >> q >> m;
    for(i = 0;i < 15;i++){
        pow3[i] = pow(3, i);
    }
    for(i = 0;i < q;i++){
        cin >> s;
        for(j = 0;j < m; j++){
            l += stoi(s[j]) * pow3[j];
        }
        cout << dp[l];
        if(dp[l] == 0){
            que.push(l);
            while(!que.empty()){
                mask = que.front(); que.pop();
                for(k = 0; k < m; k++){
                    if(check(mask, k)){
                        if(dp[mask-pow3[k]]) continue;
                        dp[mask-pow3[k]] = 1;
                        que.push(mask-pow3[k]);
                    }
                }
            }
        }
    }
}