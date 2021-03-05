import shutil
import os

# The below is the syntax for copy file.
# shutil.copy(src_file, dest_file, *, follow_symlinks=True)

src = r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\Library\SRC\fromSrc.txt'
dst =  r'C:\Users\10900225\Documents\Witch\BTX\Workspaces\Library\DST\fromSrc.txt'
shutil.copyfile(src, dst)