#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)

typedef long long tipo;
typedef long double ld;
typedef long long ll;

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

    int t; cin >> t;
    while(t--) {
        ll x1, y1, x2, y2, x3, y3;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        Punto p1(x1, y1), p2(x2, y2), p3(x3, y3);
        Punto v1 = p2 - p1;
        Punto v2 = p3 - p2;
        if ((v1 ^ v2) == 0) {
            cout << "TOUCH\n";
        } else if ((v1 ^ v2) < 0) {
            cout << "RIGHT\n";
        } else {
            cout << "LEFT\n";
        }
    }

    return 0;
}