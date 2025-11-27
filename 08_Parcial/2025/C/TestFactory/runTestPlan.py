# Execute in terminal each line of testplan.txt

import sys, os

with open("testplan.txt", "r") as f:
    for line in f:
        if line[0] == "#":
            continue
        os.system(line)