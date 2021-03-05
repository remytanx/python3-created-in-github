import os

# Get the list of all files with a specific extension
# In this example, we will take a path of a directory and try to 
# list all the files, with a specific extension .py here, 
# in the directory and its sub-directories recursively.

path = r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\Library'

for root, dirs, files in os.walk(path):
	for file in files:
		if(file.endswith(".py")):
			print(os.path.join(root,file))