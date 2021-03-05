import os

# This is where to define the path and the last word is the folder name.
# If the folder name is not present the code will generate a new folder 
# with the name.
dirPath = 'C:/Users/10900225/Documents/Witch/BTX/Workspaces/Library/DST'


if not os.path.isdir(dirPath):
    print('The directory is not present. Creating a new one..')
    os.mkdir(dirPath)
else:
    print('The directory is present.')