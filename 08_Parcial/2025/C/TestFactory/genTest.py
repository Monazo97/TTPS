import sys
import random

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
    for _ in range(N):
        a = random.randint(minValue, maxValue)
        b = random.randint(minValue, maxValue)
        if a > b:
            a, b = b, a
        f.write(f"{a} {b}\n")
