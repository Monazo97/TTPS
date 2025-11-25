import sys
import random

idTest = sys.argv[1]
N = int(sys.argv[2])
type = int(sys.argv[3])

minValue = -10**6
maxValue = 10**6

if sys.argv[4:]:
    minValue = int(sys.argv[4])
    
if sys.argv[5:]:
    maxValue = int(sys.argv[5])

#Concatenate all argv and use it as seed
seed = "".join(sys.argv[1:])
random.seed(seed)


if type == 0: # Easy version
    # Create a list of N random integers between minValue and maxValue all distinct
    arr = random.sample(range(minValue, maxValue + 1), N)
    # Randomly shuffle the list
    random.shuffle(arr)
    with open("../Tests/Test_{:02d}.in".format(int(idTest)), "w") as f:
        f.write(str(N) + "\n")
        for i in range(N):
            f.write(f"{arr[i]} 0\n")
elif type == 1: # Hard version
    # Create a list of N tuples (x,y) where x and y are a random integer between minValue and maxValue
    # No tuple should be repeated
    arr = set()
    while len(arr) < N:
        x = random.randint(minValue, maxValue)
        y = random.randint(minValue, maxValue)
        arr.add((x,y))
    arr = list(arr)
    random.shuffle(arr)
    with open("../Tests/Test_{:02d}.in".format(int(idTest)), "w") as f:
        f.write(str(N) + "\n")
        for i in range(N):
            f.write(f"{arr[i][0]} {arr[i][1]}\n")