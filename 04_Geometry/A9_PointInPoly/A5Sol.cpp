#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)

typedef long double ld;
typedef long long tipo;
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

bool pointInPoly(const Punto &q, const vector<Punto> &poly) {
    int n = poly.size();
    int cont = 0;
    for(int i = 0; i < n; i++) {
        Punto p1 = poly[i];
        Punto p2 = poly[(i+1)%n];
        if(p1.y == p2.y) continue;
        if(q.y == p2.y) continue;
        int cond = (p1.y < p2.y) ? 1 : -1;
        if(q.y < min(p1.y, p2.y) || q.y > max(p1.y, p2.y)) continue;
        if(((p2 - p1) ^ (q - p1)) * cond > 0) {
            cont++;
        }
    }
    if(cont % 2 == 1) {
        return true;
    } else {
        return false;
    }
}

int main() {
    FIN;
    
    int n, m;
    cin >> n >> m;
    vector <Punto> v(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i].x >> v[i].y;
    }

    for(int i = 0; i < m; i++) {
        Punto q;
        cin >> q.x >> q.y;
        bool border = false;
        for(int i = 0; i < n; i++) {
            Punto vec = v[(i+1)%n] - v[i];
            Punto w = q - v[(i+1)%n];
            if((vec ^ w) == 0) {
                if(q.x >= min(v[i].x, v[(i+1)%n].x) && q.x <= max(v[i].x, v[(i+1)%n].x) &&
                   q.y >= min(v[i].y, v[(i+1)%n].y) && q.y <= max(v[i].y, v[(i+1)%n].y)) {
                    border = true;
                }
            }
        }
        if(border) {
            cout << "BOUNDARY\n";
            continue;
        }
        bool check = pointInPoly(q, v);
        if(check) {
            cout << "INSIDE\n";
        } else {
            cout << "OUTSIDE\n";
        }
    }

    return 0;
}