import sys
import random

random.seed(22)

firstTest = int(sys.argv[1])
lastTest = int(sys.argv[2])

maxQ = 100
maxX = 10**6

for test in range(firstTest, lastTest + 1):
    with open(f"Tests/test{test:02d}.in", "w") as f:
        q = random.randint(1, maxQ)
        f.write(f"{q}\n")
        for _ in range(q):
            x = random.randint(2, maxX)
            f.write(f"{x}\n")