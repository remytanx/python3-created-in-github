import os


# folder_location = 'D:\\'
folder_location = 'C:/Users/10900225/Documents'

def create_file_list_v1(path):
    return_list = []

    for filenames in os.walk(path):
        for file_list in filenames:
            for file_name in file_list:
                # if file_name.endswith((".vmx")):
                if file_name.endswith((".txt")):
                    return_list.append(file_name)

        return return_list

# file_list = create_file_list(folder_location)
# print(file_list)

rootdir = os.getcwd()

print(f"rootdir: {rootdir}")

# rootdir = 'D:\\'
# outfile = 'VirtualMachinesList.txt'

rootdir = folder_location
outfile = 'test.txt'

counter = 0

def create_file_list(rootdir):
    global counter

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # print(os.path.join(subdir, file))
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                print (filepath)
                target.write(filepath + "\n")
                counter += 1

target = open(outfile, 'w')

create_file_list(rootdir)

target.write(f"\nTotal number of VMX: {counter}.")

target.close() 