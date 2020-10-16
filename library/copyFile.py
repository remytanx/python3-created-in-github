# Example
### ###
# shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
# shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext

import shutil, os, platform

uname = platform.uname()

if(uname.node == "P_IFSLT861"):
    # path = "C:\\Users\\kht79\\Documents\\Test Src Folder"
    path = "projects\miniporject"
else:
    print("Machine not found!")

print("Path at terminal when executing this command")
print(os.getcwd() + "\n")

# Change folder
os.chdir(path)

print("Path at terminal when executing this command")
print(os.getcwd() + "\n")