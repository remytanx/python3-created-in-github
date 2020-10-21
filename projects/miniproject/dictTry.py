# inPath = "projects/miniproject/dict.txt"
inPath = "projects/miniproject/infile.txt"

d = {}

with open(inPath) as f:
    for line in f:
        (key,val) = line.split('\t')
        d[int(key)] = val

print (d)