import pandas
import datetime

#   Apparently, this is the full path.
#   Why is this not using the directory that the code is it?
#   Weird.
filepath = '/Users/remytan/Documents/Project Make Life Easier/python3-created-in-github/emailtemplate/DDA_SampleCSV Corrected Copy.csv'

fread = pandas.read_csv(filepath)
freaddf = pandas.DataFrame(fread, columns=['startDateTime'])

# print(freaddf['startDateTime'].values[0])
#   Output below
#   Jan 1, 2022, 00:00:00 AM

# print(thisdate)
#   Output below
#   Jan 1, 2022, 00:00:00 AM

#   Here is trying to convert datetime using strptime()
def convert(date_time):
    format = '%b %d, %Y, %I:%M:%S %p' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

#   Driver code
# date_time = 'Dec 4 2018 10:07AM'
# date_time = 'Dec 4, 2018, 10:07:00 AM'
date_time = 'Jan 1, 2022, 12:00:00 AM'
print(f'#################')
# print(f'date_time: {date_time}')
# print(f'type of date_time:{type(date_time)}')
# print(convert(date_time))
# converted = convert(date_time)
# print(f'converted date_time: {converted}')
# print(f'type of converted date_time: {type(converted)}')

# thisdate = freaddf['startDateTime'].values[0]
thisdate = freaddf['startDateTime'].values[0]
strThisDate = freaddf['startDateTime'].apply(str)
# val1 = strThisDate.values[0]

# print(convert(thisdate))
# print(strThisDate)
print(strThisDate.values[0])
print(f'thisdate: {thisdate}')
print(f'type of thisdate: {type(thisdate)}')
convertThisDate = convert(thisdate)
print(f'converted thisdate: {convertThisDate}')
print(f'type of converted thisdate: {type(convertThisDate)}')
# print(f'strThisDate: {strThisDate}')
# print(f'type of strThisDate: {type(strThisDate)}')
print(f'#################')
# print(type(val1))
# print(convert(strThisDate.values[1]))
# print(convert(val1))

# Current issue is to convert the below into the format of dd/mm/yyyy HH:MM:SS
# e.g.: 01/01/2022 00:02:00

#   The below is a stupid mistake which made me debug for a long time..
#   There is no such format..
#   Hence the compiler keep throwing stupid error..
#   in _strptime
#     raise ValueError("time data %r does not match format %r" %
# ValueError: time data 'Jan 1, 2022, 00:00:00 AM' does not match format '%b %d, %Y, %I:%M:%S %p'

#               startDateTime
# 0  Jan 1, 2022, 00:00:00 AM
# 1  Jan 1, 2022, 00:01:00 AM
# 2  Jan 1, 2022, 00:02:00 AM
# 3  Jan 1, 2022, 00:04:00 AM
# 4  Jan 1, 2022, 00:00:00 AM
# 5  Jan 1, 2022, 00:01:00 AM
#   The above is really damn stupid!!!
#   Where in the world have 00:00:00 AM<--- de?!

#               startDateTime
# 0  Jan 1, 2022, 12:00:00 AM
# 1  Jan 1, 2022, 12:01:00 AM
# 2  Jan 1, 2022, 12:02:00 AM
# 3  Jan 1, 2022, 12:04:00 AM
# 4  Jan 1, 2022, 12:00:00 AM
# 5  Jan 1, 2022, 12:01:00 AM




#   Important data to keep are listed below.
#   Non DBS.
#   startDateTime	eventName	categoryDescription	deviceName	srcIp	sourcePort	destIp	destinationPort	eventCount	payloadAsUTF
#   
#
#   DBS
#   destinationPort	payloadAsUTF	categoryDescription	sourcePort	protocolName	deviceName	srcIp	startDateTime	destIp	eventCount
