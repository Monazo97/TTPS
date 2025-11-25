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

bool checkConvex(const vector<Punto> &v) {
    int n = v.size();
    tipo lastCrossProduct = (v[1] - v[0]) ^ (v[2] - v[1]);
    for (int i = 0; i < n; i++) {
        Punto a = v[i];
        Punto b = v[(i + 1) % n];
        Punto c = v[(i + 2) % n];
        Punto ab = b - a;
        Punto bc = c - b;
        tipo crossProduct = ab ^ bc;
        if (crossProduct != 0) {
            if ((crossProduct > 0) != (lastCrossProduct > 0)) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    FIN;

    int n;
    cin >> n;
    vector<Punto> v(n);
    for (int i = 0; i < n; i++) {
        tipo x, y;
        cin >> x >> y;
        v[i] = Punto(x, y);
    }
    if(checkConvex(v)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}