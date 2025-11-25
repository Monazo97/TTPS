class Primos:
    def __init__(self, n):
        self.lista_primos = []  # lista de números primos
        self.min_primo = []  # menor primo que divide a i
        self.es_primo = []  # True si es primo
        self.criba(n)
    
    def criba(self, n):
        self.min_primo = [0] * (n + 1)
        self.es_primo = [True] * (n + 1)  # En principio son todos primos
        self.es_primo[0] = self.es_primo[1] = False  # El 0 y 1 no son primos
        
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
        
        # Asegurarse que estén hallados todos los primos
        # menores o igual a sqrt(x) en la criba
        for p in self.lista_primos:
            if x % p == 0:
                return False
        return True
    
import sys

# Print number of different prime factors of x

q = int(sys.stdin.readline())
primos = Primos(10**6+5)  

for _ in range(q):
    x = int(sys.stdin.readline())
    count = 0
    for p in primos.lista_primos:
        if p*p > x:
            break
        if x % p == 0:
            count += 1
            while x % p == 0:
                x //= p
    if x > 1:
        count += 1
    sys.stdout.write(str(count) + "\n")
