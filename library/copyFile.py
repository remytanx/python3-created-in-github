# Example
### ###
# shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
# shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext

import shutil, os, platform

uname = platform.uname()
path = ""

print("Hello World!")

if(uname.node == "P_IFSLT861"):
    # path = "C:\\Users\\kht79\\Documents\\Test Src Folder"
    path = "projects\\miniproject"
elif(uname.node == "DESKTOP-OK52HHN"):
    path = "projects\\miniproject"
else:
    print("Machine not found!")

print("Path at terminal when executing this command")
print(os.getcwd() + "\n")

# Change folder
os.chdir(path)

print("Path at terminal when executing this command")
print(os.getcwd() + "\n")

# shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
# shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
# projects\miniproject\Test Src Folder
src = "C:\\Users\\kht79\\Documents\\Hello World\\VSC-Workspaces\\git-python3\\python3-created-in-github\\projects\\miniproject\\Test Src Folder"
# src = "projects\\miniproject\\Test Src Folder"
dst = "C:\\Users\\kht79\\Documents\\Hello World\\VSC-Workspaces\\git-python3\\python3-created-in-github\\projects\\miniproject\\Test Dst Folder"
# dst = "projects\\miniproject\\Test Dst Folder"

# copytree is to copy the whole directory
shutil.copytree(src, dst)

print("Done copying...")

print("Bye bye World!")