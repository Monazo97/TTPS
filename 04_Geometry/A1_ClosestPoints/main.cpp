#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)

typedef long double ld;
typedef long double tipo;

struct Punto {
    tipo x, y;
    Punto() : x(0), y(0) {}
    Punto(tipo x, tipo y) : x(x), y(y) {}
    Punto operator+(const Punto &p) const {
        return Punto(x + p.x, y + p.y);
    }
    Punto operator-(const Punto &p) const {
        return Punto(x - p.x, y - p.y);
    }
    Punto operator*(const tipo &k) const {
        return Punto(x * k, y * k);
    }
    tipo operator^(const Punto &p) const {
        return x * p.y - y * p.x;
    }
    ld modulo() const {
        return sqrtl(x * x + y * y);
    }
};

int main() {
    FIN;
    
    int n; cin >> n;
    vector <Punto> v(n);
    for (int i = 0; i < n; i++) {
        tipo x, y; cin >> x >> y;
        v[i] = Punto(x, y);
    }
    ld ans = (v[1]-v[0]).modulo();
    for(int i = 0; i < n; i++) {
        for(int j = i+1; j < n; j++) {
            Punto diff = v[j] - v[i];
            ans = min(ans, diff.modulo());
        }
    }
    cout << fixed << setprecision(10) << ans << "\n";

    return 0;
}