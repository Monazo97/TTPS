import sys

# Hacer una función lambda que lea un entero
read_int = lambda: int(sys.stdin.readline())

def main():
    dig = []
    cur = 1
    while len(dig) < int(1e7) + 5:
        aux = []
        copia = cur
        cur += 1
        while copia:
            aux.append(copia % 10)
            copia //= 10
        aux.reverse()
        for u in aux:
            dig.append(u)
    
    q = read_int()
    for _ in range(q):
        x = read_int()
        print(dig[x - 1])

if __name__ == "__main__":
    main()
