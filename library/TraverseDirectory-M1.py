import os

# Get the list of all files
# In this example, we will take a path of a directory and 
# try to list all the files in the directory and 
# its sub-directories recursively.

# path = r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\Library'
path = r'C:\Users\10900225\Documents'
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
for name in filelist:
    print(name)