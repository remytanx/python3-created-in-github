import re

print("Hello World!")
inPath = "projects\\miniproject\\infile.txt"
# target = open(path)
input = ""
list1 = ""
d = {}

def readFile(file):
    print("Reading from file...")
    # print(target.read())
    # pass
    target = open(file)
    return target

def assignToList(input):
    # pass
    text = input.read()
    text = re.sub(r"\s{2,}", "\t", text)
    text = text.replace('\n','\t')
    # out = open("out1.txt",'w')
    # out.write(text)
    # out.close()
    print("### re.sub + replace ###")
    print(text)
    tList = text.split('\t')
    print("=== === ===")
    print(tList)
    print(f"Length of list: {len(tList)}")
    tList.pop()
    # tList = re.split(';|\n',text)
    return tList

def readFileV2(input):
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

        return line

# input = readFile(path)
# list1 = assignToList(input)
# print(input.read())
# print(list1)
# print(dir(input))
print("Bye bye World!")