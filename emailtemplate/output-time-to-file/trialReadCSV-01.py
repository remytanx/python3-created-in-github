import csv

#   Apparently, this is the full path.
#   Why is this not using the directory that the code is it?
#   Weird.
filepath = '/Users/remytan/Documents/Project Make Life Easier/python3-created-in-github/emailtemplate/employee_birthday.txt'

#
#   This part is to read CSV file.
#   Using import csv
#

# with open('\\emailtemplate\\employee_birthday.txt') as csv_file:
with open(filepath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')