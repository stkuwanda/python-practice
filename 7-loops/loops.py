# loops or iterative statements

# range function
# range(n)
# where n is +/- integers representing an index
# starts at 0 and ends at <n
# increments by 1
print(list(range(5)))

# range function
# range(-5)
# negative integer argument yields no digits
print(list(range(-5)))

# range(1, n)
# where n is +/- integers representing an index
# starts at 1 and ends at <n
# increments by 1
print(list(range(1, 5)))

# range(1, n, 2)
# where n is +/- integers representing an index
# starts at 1 and ends at <n
# increments by 2
print(list(range(1, 5, 2)))

# range(100, n<100, -m)
# where n is a +/- integer representing an index less than 100
# where -m is a - integer such as -2
# starts at 100 and ends at >n
# decrements by m
print(list(range(100, 1, -5)))

# for loop
for i in range(5):
    print(i)
    print('number:', i)
for i in range(100, 0, -1):
    print(i)
for i in range(1, 101, 2):
    print(i)

# range() func generates a sequence of numbers. It’s commonly used with for
# loops to repeat actions a specific number of times.
# range() returns a range object, which is lazy — it doesn’t generate all numbers at once.
print('range func returns a range obj:', range(5))
# a range object can be converted to a list using a list func
print('convert a range obj to a list:', list(range(5)))

# use range func in the following ways
# range(stop)               # starts at 0, ends before stop
# range(start, stop)        # starts at start, ends before stop
# range(start, stop, step)  # starts at start, ends before stop, increments by step
