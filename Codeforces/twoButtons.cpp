#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    int clicks = 0;
    cin >> n >> m;

    while(m > n){
        if (m%2 != 0){
            m += 1;
        }
        else{
            m /= 2;
        }
        clicks += 1;
    }

    clicks += n-m;
    cout << clicks << "\n";
    return 0;
}