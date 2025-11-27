class Primos:
    def __init__(self, n):
        self.lista_primos = []  # lista de numeros primos
        self.min_primo = []  # menor primo que divide a i
        self.es_primo = []  # True si es primo
        self.criba(n)
    
    def criba(self, n):
        self.min_primo = [0] * (n + 1)
        self.es_primo = [True] * (n + 1)
        self.es_primo[0] = self.es_primo[1] = False  # El 1 no es primo
        
        for i in range(2, n + 1):
            if not self.es_primo[i]:
                continue
            self.lista_primos.append(i)
            j = i * i
            while j <= n:
                if self.es_primo[j]:
                    self.es_primo[j] = False
                    self.min_primo[j] = i
                    # i es el menor primo que divide a j
                j += i
    
    def test_primalidad(self, x):
        if x < len(self.es_primo):
            return self.es_primo[x]
        # Asegurarse que esten hallados todos los primos
        # menores o igual a sqrt(x) en la criba
        for p in self.lista_primos:
            if x % p == 0:
                return False
        return True


def BS(v, x):
    l = -1
    r = len(v)
    while r - l > 1:
        med = (l + r) // 2
        if v[med] >= x:
            r = med
        else:
            l = med
    return r


p = Primos(1000005)
primos = p.lista_primos

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    posr = BS(primos, r + 1)
    posl = BS(primos, l)
    print(posr - posl)
