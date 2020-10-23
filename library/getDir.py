import os
def fileAtTerm():
    print("Path at terminal when executing this file")
    print(os.getcwd() + "\n")
    print("This file path, relative to os.getcwd()")
    print(__file__ + "\n")

def fullPath():
    print("This file full path (following symlinks)")
    full_path = os.path.realpath(__file__)
    print(full_path + "\n")
    return full_path

def pathNFilename(full_path):
    print("This file directory and name")
    path, filename = os.path.split(full_path)
    print(path + ' --> ' + filename + "\n")

def fileDir(full_path):
    print("This file directory only")
    print(os.path.dirname(full_path))




fileAtTerm()
path = fullPath()
pathNFilename(path)
fileDir(path)