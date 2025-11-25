import os

oldTest = os.listdir("OldTests")

for file in oldTest:
    with open(os.path.join("OldTests", file), "r") as fin:
        content = fin.readlines()
    with open(os.path.join("Tests", file), "w") as fout:
        firstLine = content[0]
        n = int(firstLine.split()[0])
        fout.write(f"{n}\n")
        for i in range(1, n + 1):
            fout.write(content[i])