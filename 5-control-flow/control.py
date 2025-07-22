# control flow
a = 10
b = 20
c = 30
d = 40

# if condition:
#     statement_1
#     statement_2

# if statement
# all indented statements form part of the if statement as a block
if a > b:
    print("a is greater than b")
    print('Go ahead')
print('will always run...') # not part of if statement block

# if else statement
if b == c:
    print("b is equal to c")
else:
    print("b is not equal c")

# elif statement
if a < b:
    print("a is less than b")
elif a < c:
    print("a is less than c")
else:
    print('Something is happening with a.')