#include <bits/stdc++.h>

using namespace std;
#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0)

typedef long long ll;

// Print number of different prime factors of x

int main() {
    FIN;
    
    
    int q;
    cin >> q;
    
    for(int i = 0; i < q; i++) {
        ll x;
        cin >> x;
        int count = 0;
        ll factor = 2;
        
        while(factor * factor <= x) {
            if(x % factor == 0) {
                count++;
                while(x % factor == 0) {
                    x /= factor;
                }
            }
            factor++;
        }
        
        if(x > 1) {
            count++;
        }
        
        cout << count << "\n";
    }
    
    return 0;
}
