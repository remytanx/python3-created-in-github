import re

print("Hello World!")
path = "projects\\miniproject\\infile.txt"
# target = open(path)
input = ""
list1 = ""
def readFile(file):
    print("Reading from file...")
    # print(target.read())
    # pass
    target = open(file)
    return target

def assignToList(input):
    # pass
    text = input.read()
    text = text.replace('\n','\t')
    out = open("out1.txt",'w')
    out.write(text)
    out.close()
    print(text)
    tList = text.split('\t')
    print(tList)
    print(f"Length of list: {len(tList)}")
    tList.pop()
    tList = re.split(';|\n',text)
    return tList

input = readFile(path)
list1 = assignToList(input)
# print(input.read())
# print(list1)
# print(dir(input))
print("Bye bye World!")