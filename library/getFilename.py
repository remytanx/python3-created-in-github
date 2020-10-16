import glob, os

# What is glob?
# glob mod finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are retuened in arbitrary order. No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched. This is done by using the os.listdir() and fnmatch.fnmatch() functions in the concert, and not by actually invoking a subshell. Note that unlike, fnmatch.fnmatch(), glob treats filenames beginning with a dot (.) as special cases. (For tilde and shell variable expansion, use os.path.expanduser() and os.path.expandvars().)

# For a literal match, wrap the meta-characters in brackets. For example, '[?]' matches the character '?'.

# glob.glob(pathname)
# Return a possibly-empty list of path names that match pathname, which must be a string containing a path specification. pathname can be either absolute (like /usr/src/Python-1.5/Makefile) or relative (like ../../Tools/*/*.gif), and can contain shell-style wildcards. Broken symlinks are included in the results (as in the shell).

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