import os

# Path
path = "projects\\miniproject\\outfiles\\001-001-template.txt"

isFile = os.path.isfile(path)
print(isFile)

# Path
path = "projects\\miniproject\\outfiles\\"

isFile = os.path.isfile(path)
print(isFile)

# Path
path = "projects\\miniproject\\outfiles\\001-001-template.txt"

isFile = os.path.isdir(path)
print(isFile)

# Path
path = "projects\\miniproject\\outfiles\\"

isFile = os.path.isdir(path)
print(isFile)