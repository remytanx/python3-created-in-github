import glob, os

def stMsg():
    print("Hello World!")

def spMsg():
    print("Bye bye World!")

def getFilename():
    print("In fN getFilename")
    # pass
    os.chdir("projects\miniporject")
    for file in glob.glob("*.txt"):
        print(file)
    # print("Path at terminal when executing this file")
    # print(os.getcwd() + "\n")
    # print("This file path, relative to os.getcwd()")
    # print(__file__ + "\n")

    # print("This file full path (following symlinks)")
    # full_path = os.path.realpath(__file__)
    # print(full_path + "\n")

    # print("This file directory and name")
    # path, filename = os.path.split(full_path)
    # print(path + ' --> ' + filename + "\n")

    # print("This file directory only")
    # print(os.path.dirname(full_path))

stMsg()

getFilename()

spMsg()