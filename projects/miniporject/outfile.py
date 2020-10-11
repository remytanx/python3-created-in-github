print("Hello World!")
counter = 0

def number():
    # This is to increment the number in the filename.
    counter = 1
    print(f"Counter at {counter}.")

    # This is the loop for the number of files.
    while counter < 5:
        print(f"Counter at {counter}.")

        counter = counter + 1


    print(f"Counter at {counter}.")

    return counter

# counter = number()

def concat():
    # Test strings to concentate.
    word1 = "luer"
    word2 = counter
    word3 = "template.txt"

    output = "Hello World"

    print(f"This is {output}")
    print(word1,word2,word3)
    # print(f"This is {createfile}")

# This is to create file and it works. Commented to test the writing and formatting of filename.
# target = open(createfile,'w')
# target.close()

print("Bye bye World!")