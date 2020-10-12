import re

print("Hello World!")
path = 'projects\\miniporject\\test1.txt'
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
    text = str.replace('\n',';')
    tList = text.split(";")
    # tList = re.split(';|\n',text)
    return tList

input = readFile(path)
list1 = assignToList(input)
print(input.read())
print(list1)
# print(dir(input))
print("Bye bye World!")