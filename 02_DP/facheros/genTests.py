import random

ntest = 1
for i in range(10):
    with open(f"Tests/test-{ntest:02d}.in", "w") as f:
        f.write(f"{random.randint(1, 100000)}\n")
    ntest += 1

for i in range(10):
    with open(f"Tests/test-{ntest:02d}.in", "w") as f:
        f.write(f"{random.randint(1, 10**18)}\n")
    ntest += 1

for i in range(10):
    with open(f"Tests/test-{ntest:02d}.in", "w") as f:
        f.write(f"{10**18-i}\n")
    ntest += 1