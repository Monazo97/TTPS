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