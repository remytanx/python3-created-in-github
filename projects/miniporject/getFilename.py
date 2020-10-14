import glob, os

def stMsg():
    print("Hello World!")

def spMsg():
    print("Bye bye World!")

def getFilename():
    print("In fN getFilename")
    # pass
    os.chdir("projects\\miniporject")
    for file in glob.glob("*.txt"):
        print(file)

stMsg()

getFilename()

spMsg()