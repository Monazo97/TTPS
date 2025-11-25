import os, sys
import subprocess

sol = sys.argv[1]  # Solution to test
ejec,lang = sol.split(".")[0],sol.split(".")[1]

# Test execution script
tests = os.listdir("Tests/")
if not os.path.exists("Outputs"):
    os.mkdir("Outputs")

if not os.path.exists("Outputs/" + ejec + "_" + lang):
    os.mkdir("Outputs/" + ejec + "_" + lang)

print("Compiling " + ejec + "..." )
if lang == 'cpp':
    subprocess.run(['bash', '-i', '-c', 'compile ' + ejec], shell=False)

print("Running " + ejec + "..." )
for test in tests:
    if lang == 'cpp':
        subprocess.run(['bash', '-i', '-c', './' + ejec + ' < Tests/' + test + ' > Outputs/' + ejec + '_' + lang + '/' + test.replace(".in", ".out")], shell=False)
    elif lang == 'py':
        subprocess.run(['bash', '-i', '-c', 'python ' + ejec + '.py < Tests/' + test + ' > Outputs/' + ejec + '_' + lang + '/' + test.replace(".in", ".out")], shell=False)