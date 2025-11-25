#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0)

int main() {
    FIN;

    vector <int> dig;
    int cur = 1;
    while(dig.size() < 1e7+5) {
        vector <int> aux;
        int copia = cur++;
        while(copia) {
            aux.push_back(copia%10);
            copia /= 10;
        }
        reverse(aux.begin(),aux.end());
        for(int u : aux) dig.push_back(u);
    }
    // for(int i = 0; i < 100; i++) cerr << dig[i];
    // cerr << endl;
    int q; cin >> q;
    while(q--) {
        int x; cin >> x;
        cout << dig[x-1] << "\n";
    }

    return 0;
}