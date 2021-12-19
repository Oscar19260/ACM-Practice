#include <bits/stdc++.h>

#define MIN_SCULPTURES 3

using namespace std;

typedef unsigned int u32;

int main() {
    // faster input and output
    ios::sync_with_stdio(0);
    cin.tie(0);

    u32 n;
    cin >> n;
    
    int sculptures[n];
    int max_sum = 0;

    bool all_positive = true;

    for (u32 i = 0; i < n; i++) {
        int t;
        cin >> t;

        if (t < 0 && all_positive) {
            all_positive = false;
        }

        max_sum += t;

        sculptures[i] = t;
    }

    if (!all_positive) {
        u32 max_idx = n - 1;

        for (u32 i = max_idx; i >= MIN_SCULPTURES; i--) {
            if (n % i == 0) {
                u32 rotations = n / i;

                for (u32 j = 0; j < rotations; j++) {
                    int new_sum = 0;

                    for (u32 k = j; k <= max_idx; k += rotations) {
                        new_sum += sculptures[k];
                    }

                    if (new_sum > max_sum) {
                        max_sum = new_sum;
                    }
                }
            }
        }
    }

    cout << max_sum << '\n';

    return 0;
}
