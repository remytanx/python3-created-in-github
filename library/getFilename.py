import glob, os

def stMsg():
    print("Hello World!")

def spMsg():
    print("Bye bye World!")

def getFilename():
    print("In fN getFilename")
    # pass
    print("### ### ### ###")
    # os.chdir("projects\\miniporject")
    os.chdir("C:\\Users\\kht79\\Documents")
    for file in glob.glob("*.pdf"):
        print(file)
    print("### ### ### ###")
stMsg()

getFilename()

spMsg()