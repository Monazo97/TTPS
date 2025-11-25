from random import randint, seed

seed(1010)
tests = 2

for test in range(tests):
    t = 100000
    with open("Tests/test{}.in".format(test), "w") as f:
        f.write(str(t) + "\n")
        for _ in range(t):
            n = randint(1, 1000)
            m = randint(0, n)
            f.write("{} {}\n".format(n, m))