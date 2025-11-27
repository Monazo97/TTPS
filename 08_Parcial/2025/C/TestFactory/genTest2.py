import sys
import random
from math import sqrt

idTest = sys.argv[1]
N = int(sys.argv[2])

minValue = 1
maxValue = 10**5

if sys.argv[3:]:
    minValue = int(sys.argv[3])
    
if sys.argv[4:]:
    maxValue = int(sys.argv[4])

#Concatenate all argv and use it as seed
seed = "".join(sys.argv[1:])
random.seed(seed)

with open("../Tests/Test_{:02d}.in".format(int(idTest)), "w") as f:
    f.write(str(N) + "\n")
    D = maxValue - minValue + 1
    # Create random list of N numbers between minValue and maxValue allowing duplicates
    lista = []
    for i in range(N):
        start = min(max(1, i // int(sqrt(D))), maxValue)
        end = min(start + i // int(sqrt(D)), maxValue)
        a = random.randint(start, end)
        lista.append(a)
    f.write(" ".join(map(str, lista)) + "\n")
