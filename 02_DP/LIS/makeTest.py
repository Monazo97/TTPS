import random

def generar_permutacion_aleatoria(elementos, semilla=None):
    if semilla is not None:
        random.seed(semilla)
    
    return random.sample(elementos, len(elementos))

# Ejemplo de uso
if __name__ == "__main__":
    # Fijar semilla para reproducibilidad
    random.seed(42)
    
    # Ejemplo con números
    numeros = list(range(1,1001))
    
    for i in range(20):
        test = 4 + i
        numeros = generar_permutacion_aleatoria(numeros)
        with open(f"{test:02d}.in", "w") as f:
            f.write(f"{len(numeros)}\n")
            f.write(" ".join(map(str, numeros)) + "\n")
    