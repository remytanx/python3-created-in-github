import pandas
import datetime

#   Apparently, this is the full path.
#   Why is this not using the directory that the code is it?
#   Weird.
filepath = '/Users/remytan/Documents/Project Make Life Easier/python3-created-in-github/emailtemplate/DDA_SampleCSV Corrected Copy.csv'

fread = pandas.read_csv(filepath)
freaddf = pandas.DataFrame(fread, columns=['startDateTime'])

#   Here is trying to convert datetime using strptime()
def convert(date_time):
    format = '%b %d, %Y, %I:%M:%S %p' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

date_time = 'Jan 1, 2022, 12:00:00 AM'
print(f'#################')

thisdate = freaddf['startDateTime'].values[0]
strThisDate = freaddf['startDateTime'].apply(str)

print(strThisDate.values[0])
print(f'thisdate: {thisdate}')
print(f'type of thisdate: {type(thisdate)}')
convertThisDate = convert(thisdate)
print(f'converted thisdate: {convertThisDate}')
print(f'type of converted thisdate: {type(convertThisDate)}')

finalDate = convertThisDate.strftime('%d/%m/%Y %H:%M:%S')

print(f'finalDate: {finalDate}')
print(f'#################')

#   Output below
#################
# Jan 1, 2022, 12:00:00 AM
# thisdate: Jan 1, 2022, 12:00:00 AM
# type of thisdate: <class 'str'>
# converted thisdate: 2022-01-01 00:00:00
# type of converted thisdate: <class 'datetime.datetime'>
#################

# Current issue is to convert the above into the format of dd/mm/yyyy HH:MM:SS
# e.g.: 01/01/2022 00:02:00

finalDate = convertThisDate.strftime('%d/%m/%Y %H:%M:%S')

print(f'finalDate: {finalDate}')
print(f'#################')

#   Output below
#################
# Jan 1, 2022, 12:00:00 AM
# thisdate: Jan 1, 2022, 12:00:00 AM
# type of thisdate: <class 'str'>
# converted thisdate: 2022-01-01 00:00:00
# type of converted thisdate: <class 'datetime.datetime'>
# finalDate: 01/01/2022 00:00:00 <--- Achieved!
#################


#   Important data to keep are listed below.
#   Non DBS.
#   startDateTime	eventName	categoryDescription	deviceName	srcIp	sourcePort	destIp	destinationPort	eventCount	payloadAsUTF
#   
#
#   DBS
#   destinationPort	payloadAsUTF	categoryDescription	sourcePort	protocolName	deviceName	srcIp	startDateTime	destIp	eventCount
