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
        if x == 1:
            return 0
        div = 2
        while div * div <= x:
            if x % div == 0:
                return 0
            div += 1
        return 1


primos = Primos(1000005)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ans = 0
    for i in range(l, r + 1):
        if primos.test_primalidad(i):
            print(i)
        ans += primos.test_primalidad(i)
    print(ans)
