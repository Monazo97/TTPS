import random

random.seed(22)
nTestRand = 10
nTestMax = 10
minN = 2
maxN = 2000

for i in range(nTestRand):
    n = random.randint(minN, maxN)
    points = set()
    while len(points) < n:
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        points.add((x, y))
    with open(f'Tests/test_{i+4:02d}.in', 'w') as f:
        f.write(f"{n}\n")
        for x, y in points:
            f.write(f"{x} {y}\n")

for i in range(nTestMax):
    n = maxN
    points = set()
    while len(points) < n:
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        points.add((x, y))
    with open(f'Tests/test_{i+14:02d}.in', 'w') as f:
        f.write(f"{n}\n")
        for x, y in points:
            f.write(f"{x} {y}\n")
