print("Hello World!")
counter = 0
limit = 0

def number(limit):
    # This is to increment the number in the filename.
    counter = 1
    word = str(counter).zfill(3)
    print(f"Counter at {counter}.")
    print(f"Limit at {limit}")
    # print(f"Counter at {word}.")

    # This is the loop for the number of files.
    # while counter < 10:
    while int(counter) < int(limit):
        word1 = "luer"
        word2 = str(counter).zfill(3)
        word3 = "template.txt"
        filename = word1 + "-" + word2 + "-" + word3
        # print(f"Counter at {counter}.")
        # print(f"Counter at {word}.")
        # Printing out the sample filename by concentating in an output
        # print(f"{word1}-{word2}-{word3}")
        # Printing out the sample filename from a single string
        # print(f"Filename is {filename}")

        target = open(filename,'w')
        target.close()
        counter = counter + 1

    print(f"Counter at {counter}.")
    print(f"Limit at {limit}")
    # print(f"Counter at {word}.")
    
    # return counter
    return word

def concat(limit):
    # Test strings to concentate.
    word1 = "luer"
    word2 = limit
    word3 = "template.txt"

    # output = "Hello World"

    # print(f"This is {output}")
    print(word1,word2,word3)
    # print(f"This is {createfile}")

def createFile():

    # number(limit)
    
    # This is to create file and it works. Commented to test the writing and formatting of filename.
    # target = open(createfile,'w')
    # target.close()
    
    pass

def leadZeroTest():
    # This is how you add leading zeros
    num = 3
    word = ""
    # Converting integer into string
    word = str(num).zfill(3)

    # Printing out integer variable leading zeros but not storing them.
    print(f"num = {num:03d}.")
    print('%(num)03d.' % {"num":3})

    # Printing stored variable and this is in string.
    print(f"The word is {word}.")

limit = input(">")
# createFile()
number(limit)
# counter = number()

print("Bye bye World!")