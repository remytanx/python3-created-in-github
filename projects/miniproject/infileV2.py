import re

print("Hello World! infile.py")
inPath = ''

d = {}
o = {}
counter = 1

def readFile(input):
    with open(inPath) as f:
        for line in f.readlines():
            line = re.sub(r"\s{2,}", "\t", line)
            # print(line)
            line = line.replace(' ', '-')
            print(line)
            # line = line.rstrip("\n").split("\t")
            key, value = line.rstrip("\n").split('\t')
            d[key] = value
            # print(f"{counter}. {line}")
            # counter = counter + 1
        return d

# readFile(inPath)
# o = readFile(inPath)
# print(d)
# print(o)

print("Bye bye World! infile.py")