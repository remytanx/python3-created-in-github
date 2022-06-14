import pandas
import datetime

#   Apparently, this is the full path.
#   Why is this not using the directory that the code is it?
#   Weird.
filepath = '/Users/remytan/Documents/Project Make Life Easier/python3-created-in-github/emailtemplate/DDA_SampleCSV Copy.csv'

#
#   This part is to read CSV file.
#   Using import csv
#

#   This worked and printed all columns
#   [6 rows x 84 columns]
df = pandas.read_csv(filepath)
testdf = pandas.DataFrame.head(df,n=1)

# print(df)
print(testdf)

# df = pandas.read_csv(filepath, 
#             index_col='startDateTime',
#             header=0,
#             parse_dates=['startDateTime'])
# print(df)
#   End

# fread = pandas.read_csv(filepath)
# freaddf = pandas.DataFrame(fread, columns=['startDateTime'])

# print(freaddf)
#   Output below
#               startDateTime
# 0  Jan 1, 2022, 00:00:00 AM
# 1  Jan 1, 2022, 00:01:00 AM
# 2  Jan 1, 2022, 00:02:00 AM
# 3  Jan 1, 2022, 00:04:00 AM
# 4  Jan 1, 2022, 00:00:00 AM
# 5  Jan 1, 2022, 00:01:00 AM
#   End

# print(freaddf.loc[1])
#   Output below
# startDateTime    Jan 1, 2022, 00:01:00 AM
# Name: 1, dtype: object
#   End

# print(list(freaddf))
#   Output below
#   ['startDateTime']

# print(list(freaddf)[0])
#   Output below
#   startDateTime

# print(freaddf['startDateTime'].values[0])
#   Output below
#   Jan 1, 2022, 00:00:00 AM

# print(freaddf['startDateTime'].values[1])
#   Output below
#   Jan 1, 2022, 00:01:00 AM

# print(freaddf['startDateTime'].values[2])
#   Output below
#   Jan 1, 2022, 00:02:00 AM

#   Removing indexing and column names..
#   This works too..
#   Maybe useful..
# dfstr   = freaddf.to_string(index = False) # Make str, possibly remove index
# dfrows  = dfstr.split('\n')           # split on rows
# dfprint = dfrows[1:]                  # Do not print row 0 (columns)
# dfp     = '\n'.join(dfprint)          # Create a single string again

# print(dfp)

# dfstr   = freaddf.to_string(index = False) # Make str, possibly remove index
# dfrows  = dfstr.split('\n')           # split on rows
# dfprint = dfrows[1]                  # Do not print row 0 (columns)
# dfp     = '\n'.join(dfprint)          # Create a single string again

# print(dfp)

#   Output below
# Jan 1, 2022, 00:00:00 AM
# Jan 1, 2022, 00:01:00 AM
# Jan 1, 2022, 00:02:00 AM
# Jan 1, 2022, 00:04:00 AM
# Jan 1, 2022, 00:00:00 AM
# Jan 1, 2022, 00:01:00 AM
#   End




#   End

# Current issue is to convert the below into the format of dd/mm/yyyy HH:MM:SS
# e.g.: 01/01/2022 00:02:00

#               startDateTime
# 0  Jan 1, 2022, 00:00:00 AM
# 1  Jan 1, 2022, 00:01:00 AM
# 2  Jan 1, 2022, 00:02:00 AM
# 3  Jan 1, 2022, 00:04:00 AM
# 4  Jan 1, 2022, 00:00:00 AM
# 5  Jan 1, 2022, 00:01:00 AM






#   Important data to keep are listed below.
#   Non DBS.
#   startDateTime	eventName	categoryDescription	deviceName	srcIp	sourcePort	destIp	destinationPort	eventCount	payloadAsUTF
#   
#
#   DBS
#   destinationPort	payloadAsUTF	categoryDescription	sourcePort	protocolName	deviceName	srcIp	startDateTime	destIp	eventCount
