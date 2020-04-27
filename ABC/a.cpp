#include <bits/stdc++.h>

const int N = 10000001;
int mind[N];
std::vector<int> pr;

void build_sieve(){
    mind[0] = mind[1] = 1;
    for(int i=2; i<N; ++i){
        if(mind[i] == 0){
            pr.push_back(i);
            mind[i] = i;
        }
        for (int j=0; j<int(pr.size()) && pr[j]<=mind[i] && i*pr[j]<N; ++j){
            mind[i*pr[j]] = pr[j];
        }    
    }
}