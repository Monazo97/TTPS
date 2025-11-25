#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)

typedef long double ld;
typedef long long ll;
typedef long double tipo;
const ld EPS = 1e-9;

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

struct Linea {
    Punto p, v;
    Linea() {}
    Linea(const Punto &p, const Punto &q) : p(p), v(q - p) {}
    bool interseca(const Linea &l, Punto &ans) const {
        if(abs(v ^ l.v) < EPS) return false;
        tipo alpha = tipo((l.p - p)^l.v) / tipo(v^l.v);
        ans = p + v * alpha;
        return true;
    }
};



int main() {
    FIN;
    
    int t; cin >> t;
    while(t--) {
        Punto p1, p2, p3, p4;
        vector <ll> coords(8);
        for(int i = 0; i < 8; i++) cin >> coords[i];
        p1 = Punto(coords[0], coords[1]);
        p2 = Punto(coords[2], coords[3]);
        p3 = Punto(coords[4], coords[5]);
        p4 = Punto(coords[6], coords[7]);
        Linea l1(p1, p2), l2(p3, p4);
        if(fabsl(l1.v ^ l2.v) < EPS) {
            Punto check = p3 - p1;
            if(fabsl(l1.v ^ check) < EPS) {
                cout << "SAME\n";
            } else {
                cout << "PARALLEL\n";
            }
        } else {
            Punto ans;
            l1.interseca(l2, ans);
            cout << fixed << setprecision(10) << ans.x << " " << ans.y << "\n";
        }
    }

    return 0;
}