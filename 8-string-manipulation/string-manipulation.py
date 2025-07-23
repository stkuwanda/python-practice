# string indexing and slicing
# positive indices start from 0 and increment by 1
# negative indices start from -1 and decrement by 1
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