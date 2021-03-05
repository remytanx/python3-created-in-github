import os

# In the OS module, the getsize() function allows 
# to get the size of a file in bytes

def get_file_size(file_path):
    size = os.path.getsize(file_path)
    # print("size", size)
    # size = size / 1000000
    return size

file_path = r'C:\Users\10900225\Downloads\python-3.9.1-amd64.exe'
size = get_file_size(file_path)
print('File size: '+ str(size) +' bytes')
