import os, shutil
import sys

# get args

program = sys.argv[1]

inputFiles = os.listdir('Tests')

for file in inputFiles:
    # Execute program
    # print(f"Running test {file}...")
    # print(f"{program}.exe < Tests/{file} > Output/{file.replace('.in', '.out')}")
    
    os.system(f"{program}.exe < Tests/{file} > Output/{file.replace('.in', '.out')}")
