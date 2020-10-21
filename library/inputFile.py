import re

print("Hello World!")

# dictTest = {"test1":"OK1", "test2":"OK2", "test3":"OK3"}
# print(f"dictTest: {dictTest}")

# inPath = "projects/miniproject/dict.txt"
inPath = "projects/miniproject/infile.txt"

d = {}
counter = 1

def readFile(input):
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
readFile(inPath)
print (d)


print("Bye bye World!")