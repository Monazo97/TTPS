import sys

# Print number of different prime factors of x

q = int(sys.stdin.readline())

for _ in range(q):
    x = int(sys.stdin.readline())
    count = 0
    factor = 2
    while factor * factor <= x:
        if x % factor == 0:
            count += 1
            while x % factor == 0:
                x //= factor
        factor += 1
    if x > 1:
        count += 1
    sys.stdout.write(str(count) + "\n")
