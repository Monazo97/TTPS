import sys

_input, _output, _ans = sys.argv[1], sys.argv[2], sys.argv[3]
inf = open(_input, "r")
ouf = open(_output, "r")
ans = open(_ans, "r")

output_lines = ouf.readlines()
ans_lines = ans.readlines()

if len(output_lines) != len(ans_lines):
    print("Wrong Answer: number of lines differ")
    sys.exit(1)

if output_lines != ans_lines:
    print("Wrong Answer: content differs")
    sys.exit(1)

print("Accepted")
