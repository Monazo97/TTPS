# Execute in terminal each line of testplan.txt

import sys, os

with open("testplan.txt", "r") as f:
    for line in f:
        os.system(line)