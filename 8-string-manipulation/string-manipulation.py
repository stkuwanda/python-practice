# string indexing and slicing
# positive indices start from 0 and increment by 1
# negative indices start from -1 and increment by 1
str1 = 'Hello World'
print('should print o:', str1[4])
print('should print o:', str1[-7])

# slicing
print('substring from index 2 to index (5-1):', str1[2:5])
print('origin string variable str1:', str1)

# enhance slicing by introducing a custom increment value
# this will output values within the range and selected
# by the increment or skip magnitude
print('a strange substring:', str1[2:10:2])
print('another strange substring:', str1[-1:-12:-2])
print('another strange substring:', str1[0::2]) # the missing value implies the whole range is included to the last index

# string iteration
str1 = 'Welcome to python programming language'

# get string length
l = len(str1)
print('String length:', l)

# iterate through a string
for n in range(l):
    print(str1[n])

# reverse a string
str2 = str1[-1::-1]
print('reversed string:')
for n in range(len(str2)):
    print(str2[n])

# the string is an iterable sequence type in itself
print('iterate through a string')
for n in str1:
    print(n)

# common string functions

# lower case and upper case funcs
str3 = 'Hello World'
print('lower case:', str3.lower())
print('upper case:', str3.upper())

# title case
# title func capitalizes the 1st letter of each word
# and lower cases the remaining characters
str4 = 'HELLO WORLD'
print('title case:', str4.title())

# capitalize case
# capitalize func capitalizes the first character
# of the string and lower cases the rest
print('capitalize:', str4.capitalize())

# advanced string funcs
# find
# return index of search term else return -1
str5 = 'Hello World'
print('find index of l:', str5.find('l'))
print('find index of next l:', str5.find('l', 3))
print('find index of next l:', str5.find('l', 4,5))

# index
# return the index of the search term or else error
print('find index of next l:', str5.index('l', 3,4))

# isalpha func checks if string is purely alphabetic.
# spaces, digits and special characters are not alphabetic
print('str5 is alphabetic:', str5.isalpha())

# isdigit func
# returns True if string contains digits only
str6 = '233'
print('str6 is a digit:', str6.isdigit())

# isalnum func
# returns True if string contains only digits and/or alphabet chars
str7 = 'Hello123'
print('str7 is a alphanumeric:', str7.isalnum())

# chr func
# returns ascii character from an integer argument
num = 65
print(chr(num))

# ord func
# returns ascii code point from a single char
char = 'q'
print(ord(char))

# string formatting

# using placeholders
nameStr = 'My name is {firstName} {lastName}.'.format(firstName='John', lastName='Doe')

# using indices
nameStr1 = 'My name is {0} {1}.'.format('Jane', 'Doe')

# using automatic detection of indices: {} {}
nameStr2 = 'My name is {} {}.'.format('Jane', 'Doe')

# were start & stop are integer indices $ step is a skip integer.
# start indice is inclusive
# stop indice is non-inclusive
# string[start] # (at start only)

# with defaults
# string[start:]       # (from index start to end)
# string[start:stop]   # (from start to stop)
# string[:stop]        # (from start to stop)
# string[:]            # (entire string)
# string[::step]       # (every step character)
# string[start::step]  # (starting at start to end, every step character)
# string[::-1]         # (entire string in reverse)

