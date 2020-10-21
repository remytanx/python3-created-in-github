import re

# inPath = "projects/miniproject/dict.txt"
inPath = "projects/miniproject/infile.txt"

d = {}
counter = 1

with open(inPath) as f:
    for line in f.readlines():
        line = re.sub(r"\s{2,}", "\t", line)
        # print(line)
        line = line.replace(' ', '-')
        # line = line.rstrip("\n").split("\t")
        key, value = line.rstrip("\n").split('\t')
        d[key] = value
        # print(f"{counter}. {line}")
        # counter = counter + 1

print (d)