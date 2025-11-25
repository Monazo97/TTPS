/*----------------------*/
/*----- Monazo1997 -----*/
/*----------------------*/
 
#include <bits/stdc++.h>
using namespace std;
//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);
 
typedef long long ll;
#define FIN ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define forr(i, a, b) for(ll i = (a); i < (ll) (b); i++)
#define forn(i, n) forr(i, 0, n)
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define DBG(x) cerr << #x << " = " << (x) << endl
#define DBGV(v,n) forn(i,n) cout << v[i] << " "; cout << endl
#define esta(x,c) ((c).find(x) != (c).end())
#define RAYA cerr << "===============================" << endl
const ll MOD = (ll)(1e9+7); // 998244353 
const ll INF = (ll)(1e9+10); // (1e18+10)
const int MAXN = (int)(2e5+5);
 
typedef long double tipo; //Cambiar a long long para operar en enteros
double EPS = (double)(1e-10);
 
struct punto { // Puede usarse para vectores
  tipo x, y;
  punto const operator -(const punto &p) const {return {x-p.x,y-p.y};}
  punto const operator +(const punto &p) const {return {x+p.x,y+p.y};}
  tipo const operator *(const punto &p) const {return x*p.x + y*p.y;}
  tipo const operator ^(const punto &p) const {return x*p.y - y*p.x;}
  bool const operator == (const punto &p) const {
    return (abs(x-p.x) < EPS && abs(y-p.y) < EPS); // Para double
  }
  bool operator <(punto p) const {return x != p.x ? x < p.x : y < p.y;}
  tipo arg() {return atan2(y,x);} 
  tipo mod() {return sqrtl(x*x + y*y);}
  tipo mod2() {return x*x + y*y;}
};
 
punto operator*(tipo k, const punto &p) {return {k*p.x, k*p.y};}
 
ostream &operator << (ostream &os, const punto &p) { //Para imprimir
  return os << "(" << p.x << "," << p.y << ")";
}
 
istream &operator >> (istream &is, punto &p) { //Para leer
  return is >> p.x >> p.y;
}
 
 
struct recta { // Puede usarse para segmentos ([p,p+v] o alpha = [0,1])
  punto v, p; // v -> director, p -> punto por donde pasa
  recta(punto p1, punto p2) { v = (p2-p1); p = p1;}
  recta() {}
  recta(tipo A, tipo B, tipo C) { // Transform Ax + By + C = 0 
    v = {-B,A}; A != 0 ? p = {-C / A,0} : p = {0,-C / B}; 
  }
  bool is_in(punto q){return fabs((q.x-p.x)*v.y - (q.y-p.y)*v.x) < EPS;}
  punto eval(double x) {return x * v + p;}
};
 
int main(){
  FIN;
	
  int t; cin >> t;
  while(t--) {
    punto a, b, c;
    cin >> a >> b >> c;
    punto v1 = b-a;
    punto v2 = c-b;
    tipo ans = v1 ^ v2;
    if(abs(ans) < EPS) cout << "TOUCH\n";
    else if(ans > 0) cout << "LEFT\n";
    else cout << "RIGHT\n";
  }
  
  return 0;
}