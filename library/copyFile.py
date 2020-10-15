# Example
### ###
# shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
# shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext

import shutil, os

path = "C:\\Users\\kht79\\Documents\\Test Src Folder"

print("Path at terminal when executing this command")
print(os.getcwd() + "\n")

os.chdir(path)

print("Path at terminal when executing this command")
print(os.getcwd() + "\n")