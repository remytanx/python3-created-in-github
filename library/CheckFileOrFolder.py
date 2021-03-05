import os

fpath = r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\Library'

#checks if path is a file
isFile = os.path.isfile(fpath)

#checks if path is a directory
isDirectory = os.path.isdir(fpath)

print('The file present at the path is a regular file:', isFile)
print('Path points to a Directory:', isDirectory)