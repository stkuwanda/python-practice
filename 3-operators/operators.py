a = 10
b = 3
c = 4
d = 5

# arithmetic operators
print('Addition: ', a + b)
print('Subtraction: ', a - b)
print('Multiplication: ', a * b)
print('Regular Division: ', a / b)
print('Floor division: ', a // b)
print('Exponentiation: ', a ** b)
print('Modulo: ', a % b)

# assignment operators

# addition assignment
c += b
print(c)

# subtraction assignment
d -= 1
print(d)

# multiplication assignment
c *= 2
print(c)

# floor division assignment
c //= 3
print(c)

# exponent assignment
c **= 2
print(c)

# division assignment
c /= 2
print(c)

# comparison operators
print('equivalence: a == b =', a == b)
print('non-equivalence: a != b =', a != b)
print('greater: a > b =', a > b)
print('less: a < b =', a < b)
print('less_equal: a <= b =', a <= b)
print('greater_equal: a >= b =', a >= b)

# logical operators
print('and operator: ', a < b and a < 10)
print('or operator: ', a <= b or a <= 10)
print('not operator: ', not a != b)

# membership operators
string1 = 'Hello'
items = [1, 2, 3]
print("'H' in string1: ", 'H' in string1)
print('3 in items: ', 3 in items)
print('10 not in items: ', 10 not in items)

# identity operators
z = 10
print('a is b: ', a is b)
print('a is not b: ', a is not b)
print('a is z', a is z)


