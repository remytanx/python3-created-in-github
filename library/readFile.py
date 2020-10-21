import re

print("Hello World!")

dictTest = {"test1":"OK1", "test2":"OK2", "test3":"OK3"}
print(f"dictTest: {dictTest}")

inPath = "projects/miniproject/infile.txt"

d = {}

with open(inPath) as f:
    for line in f:
        (key,val) = line.split()
        d[int(key)] = val

print (d)


print("Bye bye World!")